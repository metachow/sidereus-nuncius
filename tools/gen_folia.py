"""Generate folia/*.tex and folia/order.tex from the text-first sources in text/.

usage: python tools/gen_folia.py [--lang zh] [--out folia]

zh (default) uses text/zh.yaml, translation stored per alignment block.
Any other language uses text/<lang>.yaml or all *.yaml files in text/<lang>/,
translation stored per Latin sentence ('p012.03': ...): each sentence goes to the
block, and so the page, where its Latin sentence starts. Keys naming a block
('f01r.1') give that block's translation whole; this is how blocks with special
layout (title page, headings, signatures) are translated. Missing sentences are
marked [p012.03], missing special blocks [f01r.1].
Do not edit folia/ by hand: edit text/ and regenerate.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textmodel import MARK, load_yaml, segments  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def build(lang='zh', out='folia'):
    T = os.path.join(ROOT, 'text')
    la = {p['id']: p for p in load_yaml(os.path.join(T, 'la.yaml'))}
    layout = load_yaml(os.path.join(T, 'layout.yaml'))
    trans = {}
    if os.path.exists(os.path.join(T, f'{lang}.yaml')):
        trans.update(load_yaml(os.path.join(T, f'{lang}.yaml')) or {})
    if os.path.isdir(os.path.join(T, lang)):
        for fn in sorted(os.listdir(os.path.join(T, lang))):
            if fn.endswith('.yaml'):
                trans.update(load_yaml(os.path.join(T, lang, fn)) or {})
    segs = {pid: segments(p) for pid, p in la.items()}
    if lang not in ('zh', 'ja'):
        # with ctex loaded, xeCJK treats ‘ ’ “ ” — – … as CJK punctuation (extra
        # space, line breaks after an apostrophe); write them as TeX ligatures
        tex = str.maketrans({'‘': '`', '’': "'", '“': '``', '”': "''",
                             '—': '---', '–': '--', '…': '\\ldots{}'})
        trans = {k: v.translate(tex) if isinstance(v, str) else v for k, v in trans.items()}

    def seg_text(ref):
        pid, k = ref.split(':')
        k = int(k)
        p = la[pid]
        text = segs[pid][0][k]
        if k > 0 or p.get('noindent'):
            text = '\\noindent ' + text
        return text, p.get('notes', {}).get(k)

    def seg_translation(part):
        """sentence-level translation of one Latin segment. A translated sentence goes
        whole to the segment where its Latin starts, unless it carries page-break
        markers ⟦…⟧ at the places matching the Latin's: then it is split there and
        each piece goes to the matching segment, like the Latin."""
        pid, k = part['seg'].split(':')
        k = int(k)
        _, start = segs[pid]
        sents = []
        for s, seg in start.items():
            t = trans.get(f'{pid}.{s}', f'[{pid}.{s}]')
            pieces = MARK.split(t)
            n_la = len(re.findall(r'⟦[^⟧|]+⟧', la[pid]['s'][s]))
            if len(pieces) > 1 and len(pieces) - 1 == n_la:
                if seg <= k <= seg + n_la and pieces[k - seg].strip():
                    sents.append(pieces[k - seg].strip())
            elif seg == k:
                sents.append(MARK.sub(' ', t).strip())
        if not sents:
            return ''
        text = ('\\noindent ' if k > 0 else '') + ' '.join(sents)
        if 'wrap' in part:                      # e.g. the tapered ending
            text = part['wrap'].replace('%s', text)
        return text

    def sentence_block(pair):
        """translation of a pair from sentence-level data; a special-layout part
        inside a pair is translated under the key '<pair>#<part index>'"""
        paras = []
        for i, part in enumerate(pair['la']):
            if 'seg' in part:
                text = seg_translation(part)
            elif 'raw' in part:
                text = trans.get(f"{pair['pair']}#{i}", f"[{pair['pair']}#{i}]")
            else:
                continue
            if text:
                paras.append(text)
        return '\n\n'.join(paras)

    os.makedirs(os.path.join(ROOT, out), exist_ok=True)
    order = []
    for page in layout:
        name = page['file']
        order.append(name)
        if page.get('blank'):
            body = f"\\blankfolium{{{page['folio']}}}\n"
        else:
            star = '*' if page.get('nohead') else ''
            chunks = []
            for it in page['items']:
                if 'fig' in it:
                    chunks.append(it['fig'])
                elif 'tex' in it:
                    chunks.append(it['tex'])
                else:
                    mode = it.get('mode', '')
                    la_out, glue = [], []
                    for part in it['la']:
                        if 'pre' in part:
                            glue.append(part['pre'])
                            continue
                        if 'raw' in part:
                            text = part['raw']
                        else:
                            text, note = seg_text(part['seg'])
                            if 'wrap' in part:
                                text = part['wrap'].replace('%s', text)
                            if note:
                                text += ' ' + note
                        la_out.append('\n'.join(glue + [text]))
                        glue = []
                    if glue:
                        la_out.append('\n'.join(glue))
                    if lang == 'zh':
                        tr = trans.get(it['pair'], '')
                    elif it['pair'] in trans:
                        tr = trans[it['pair']]
                    elif not any('seg' in part for part in it['la']):
                        tr = f"[{it['pair']}]"
                    else:
                        tr = sentence_block(it)
                    la_text = '\n\n'.join(la_out)
                    la_size = page.get('la_size', {}).get(lang)   # per edition and page
                    if la_size:
                        la_text = (f'\\fontsize{{{la_size[0]}}}{{{la_size[1]}}}\\selectfont'
                                   f' % fitted to one page\n' + la_text)
                    chunks.append(f'\\LA{mode}\n' + la_text)
                    # per-page tightening of the translation column (layout.yaml: tr_size)
                    size = page.get('tr_size', {}).get(lang)
                    if size:
                        tr = f'\\fontsize{{{size[0]}}}{{{size[1]}}}\\selectfont % fitted to one page\n' + tr
                    chunks.append(f'\\ZH{mode}\n' + tr)
            body = f"\\folium{star}{{{page['folio']}}}\n\n" + '\n\n'.join(chunks) + '\n\n\\folioend\n'
        with open(os.path.join(ROOT, out, name + '.tex'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('% Generated from text/ by tools/gen_folia.py -- edit text/*.yaml, not this file.\n')
            f.write(body)
    with open(os.path.join(ROOT, out, 'order.tex'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('% Generated by tools/gen_folia.py from text/layout.yaml\n')
        f.write(''.join(f'\\input{{{out}/{n}}}\n' for n in order))
    return len(order)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--lang', default='zh')
    ap.add_argument('--out', default='folia')
    a = ap.parse_args()
    print(build(a.lang, a.out), 'folia written to', a.out)
