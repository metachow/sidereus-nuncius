"""One-time migration: split the hand-written folia/*.tex into the text-first sources

  text/la.yaml      Latin, one logical paragraph per entry, one sentence per key;
                    page breaks as ⟦8v⟧ inside sentences, ⟦|⟧ where a page splits
                    a paragraph into two alignment blocks (usually around a figure)
  text/zh.yaml      Chinese, one entry per alignment block ("pair"), as written
  text/layout.yaml  per folio: page style and the ordered items (pairs, figures, raw TeX)

usage: python tools/migrate_folia.py      (reads folia/, writes text/)
Kept in the repository as a record of how the sources were derived.
"""
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textmodel import dump_yaml, split_sentences  # noqa: E402

BLOCK = {'\\LA': ('la', ''), '\\LAi': ('la', 'i'), '\\ZH': ('zh', ''), '\\ZHi': ('zh', 'i')}
CMD_LINE = re.compile(r'^\\(selectlanguage|vspace|fontsize)\b')


def read_order():
    out = []
    for line in open(os.path.join(ROOT, 'folia', 'order.tex'), encoding='utf-8'):
        m = re.match(r'\\input\{folia/(.+)\}', line.strip())
        if m:
            out.append(m.group(1))
    return out


def braced_end(text, start):
    """index just after the group that opens at text[start] == '{'"""
    depth = 0
    for i in range(start, len(text)):
        c = text[i]
        if c == '\\':
            continue
        if c == '{' and (i == 0 or text[i - 1] != '\\'):
            depth += 1
        elif c == '}' and text[i - 1] != '\\':
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError('unbalanced braces')


def parse_folio(name):
    """-> header, list of items: ('block', kind, mode, text) | ('fig', text) | ('tex', text)"""
    src = open(os.path.join(ROOT, 'folia', name + '.tex'), encoding='utf-8').read()
    lines = src.split('\n')
    header = lines[0].strip()
    items, cur, pending = [], None, []
    i = 1
    while i < len(lines):
        s = lines[i].strip()
        if s in BLOCK:
            cur = ['block', *BLOCK[s], []]
            items.append(cur)
            i += 1
            continue
        if s == '\\folioend':
            break
        if s.startswith('\\spanfig') or s.startswith('\\headpiece') or s.startswith('\\enlargethispage'):
            rest = '\n'.join(lines[i:])
            if s.startswith('\\spanfig'):
                end = braced_end(rest, rest.index('{'))
            else:
                end = len(lines[i])
            raw = rest[:end]
            # comment lines written just before a figure belong to it
            if cur is not None:
                while cur[3] and cur[3][-1].strip().startswith('%'):
                    pending.insert(0, cur[3].pop())
            items.append(['fig' if s.startswith('\\spanfig') else 'tex', '\n'.join(pending + [raw])])
            pending = []
            cur = None
            i += raw.count('\n') + 1
            continue
        if cur is not None:
            cur[3].append(lines[i])
        elif s:
            pending.append(lines[i])
        i += 1
    for it in items:
        if it[0] == 'block':
            it[3] = '\n'.join(it[3]).strip('\n')
    if pending:
        items.append(['tex', '\n'.join(pending)])
    return header, items


def classify_la(text):
    """split a Latin block into parts: ('pre', line) | ('raw', para) | ('seg', text, noindent, wrap, note)"""
    parts = []
    for para in re.split(r'\n\s*\n', text):
        if not para.strip():
            continue
        lines = para.split('\n')
        while lines and (CMD_LINE.match(lines[0].strip()) or lines[0].strip().startswith('%')) \
                and len(lines) > 1:
            parts.append(('pre', lines.pop(0)))
        body = '\n'.join(lines)
        stripped = body.strip()
        wrap = None
        m = re.match(r'^(\\taperpar(?:\[[^\]]*\])?)\{', stripped)
        if m:
            end = braced_end(stripped, m.end() - 1)
            inner = stripped[m.end():end - 1]
            tail = stripped[end:]
            wrap = m.group(1) + '{%s}'
            stripped = inner + tail
        # end-of-line comments (notes on the 1610 reading) can sit anywhere in a
        # paragraph; collect them and rejoin the text as TeX would read it
        notes, text_lines = [], []
        for ln in stripped.split('\n'):
            mm = re.search(r'(?<!\\)%.*$', ln)
            if mm:
                notes.append(mm.group(0))
                ln = ln[:mm.start()]
                text_lines.append((ln.rstrip(), ln != ln.rstrip() or not ln))
            else:
                text_lines.append((ln.strip(), True))
        joined = ''
        for t, space_after in text_lines:
            if t:
                joined += t + (' ' if space_after else '')
        note = ' '.join(notes) if notes else None
        if note and joined.strip():
            stripped = joined.strip()
        noindent = stripped.startswith('\\noindent')
        core = re.sub(r'^\\noindent\s*', '', stripped)
        flow = bool(re.match(r'([A-Za-z(]|\\(woodinitial|lettrine|capsemph|lital|textit)\b)', core)) \
            and '\n' not in core.strip()
        if flow:
            parts.append(('seg', core.strip(), noindent, wrap, note))
        else:
            parts.append(('raw', body))
    return parts


def main():
    order = read_order()
    layout, zh, paragraphs = [], {}, []
    cur_par = None          # [segments, boundaries, notes, first_noindent]
    last_folio = None
    for name in order:
        header, items = parse_folio(name)
        m = re.match(r'\\(folium\*?|blankfolium)\{(.+)\}', header)
        kind, label = m.group(1), m.group(2)
        entry = {'file': name, 'folio': label}
        if kind == 'blankfolium':
            entry['blank'] = True
            layout.append(entry)
            continue
        if kind == 'folium*':
            entry['nohead'] = True
        out_items, npair = [], 0
        k = 0
        while k < len(items):
            it = items[k]
            if it[0] in ('fig', 'tex'):
                out_items.append({it[0]: it[1]})
                k += 1
                continue
            assert it[1] == 'la', (name, it)
            nxt = items[k + 1] if k + 1 < len(items) else None
            assert nxt and nxt[0] == 'block' and nxt[1] == 'zh', (name, 'Latin block without Chinese')
            npair += 1
            pid = f'{name}.{npair}'
            pair = {'pair': pid}
            if it[2]:
                pair['mode'] = it[2]
            assert it[2] == nxt[2], (name, 'mode mismatch')
            la_parts = []
            for p in classify_la(it[3]):
                if p[0] in ('pre', 'raw'):
                    la_parts.append({p[0]: p[1]})
                    continue
                _, text, noindent, wrap, note = p
                if noindent and cur_par is not None:
                    btype = '⟦%s⟧' % label if label != last_folio else '⟦|⟧'
                    cur_par['segs'].append(text)
                    cur_par['bounds'].append(btype)
                else:
                    cur_par = {'segs': [text], 'bounds': [], 'notes': {}, 'id': f'p{len(paragraphs) + 1:03d}'}
                    if noindent:
                        cur_par['first_noindent'] = True
                    paragraphs.append(cur_par)
                seg_ref = f"{cur_par['id']}:{len(cur_par['segs']) - 1}"
                part = {'seg': seg_ref}
                if wrap:
                    part['wrap'] = wrap
                la_parts.append(part)
                if note:
                    cur_par['notes'][len(cur_par['segs']) - 1] = note
                last_folio = label
            pair['la'] = la_parts
            out_items.append(pair)
            zh[pid] = nxt[3]
            k += 2
        entry['items'] = out_items
        layout.append(entry)

    la = []
    for p in paragraphs:
        text = p['segs'][0]
        for b, s in zip(p['bounds'], p['segs'][1:]):
            text += ' ' + b + ' ' + s
        sents = split_sentences(text)
        e = {'id': p['id'], 's': {f'{i + 1:02d}': t for i, t in enumerate(sents)}}
        if p.get('first_noindent'):
            e['noindent'] = True
        if p['notes']:
            e['notes'] = {int(k): v for k, v in p['notes'].items()}
        la.append(e)

    os.makedirs(os.path.join(ROOT, 'text'), exist_ok=True)
    dump_yaml(la, os.path.join(ROOT, 'text', 'la.yaml'),
              '# Latin source: one entry per paragraph, one key per sentence.\n'
              '# ⟦8v⟧ = page break of the 1610 edition (the text after it is on folio 8v);\n'
              '# ⟦|⟧ = split into two alignment blocks on the same page (usually a figure).\n')
    dump_yaml(zh, os.path.join(ROOT, 'text', 'zh.yaml'),
              '# Chinese translation, one entry per alignment block (see layout.yaml).\n')
    dump_yaml(layout, os.path.join(ROOT, 'text', 'layout.yaml'),
              '# Pages of the 1610 edition in order: page style and the items on each page.\n'
              '# pair: one Latin block (segments of la.yaml paragraphs, "p012:1" = 2nd segment of p012)\n'
              '#       aligned with one translation block; fig / tex: raw LaTeX.\n')
    print(f'{len(layout)} folia, {len(paragraphs)} paragraphs, '
          f'{sum(len(e["s"]) for e in la)} sentences, {len(zh)} pairs')


if __name__ == '__main__':
    main()
