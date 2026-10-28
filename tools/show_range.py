"""Print a range of the Latin source for a translator, sentence by sentence, with the
Chinese edition's text for the same blocks (for its footnotes) and the special-layout
blocks that fall in the range.

usage: python tools/show_range.py p001 p013 [--no-zh]
Output is UTF-8; on Windows set PYTHONIOENCODING=utf-8.

A special block (title lines, headings, signatures; no numbered sentences) belongs
to the range of the next paragraph after it in reading order, and is translated
whole under its block key (e.g. "f04v.3").
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textmodel import load_yaml  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
a, b = sys.argv[1], sys.argv[2]
show_zh = '--no-zh' not in sys.argv
la = load_yaml(os.path.join(ROOT, 'text', 'la.yaml'))
zh = load_yaml(os.path.join(ROOT, 'text', 'zh.yaml'))
layout = load_yaml(os.path.join(ROOT, 'text', 'layout.yaml'))
ids = [p['id'] for p in la]
wanted = set(ids[ids.index(a):ids.index(b) + 1])

# reading order: assign each special block to the next paragraph
specials, pending = {}, []
blocks_of = {}
for page in layout:
    for it in page.get('items', []):
        if 'pair' not in it:
            continue
        pars = [part['seg'].split(':')[0] for part in it['la'] if 'seg' in part]
        if not pars:
            pending.append((page['folio'], it))
            continue
        for p in pars:
            blocks_of.setdefault(p, []).append(it['pair'])
        specials.setdefault(pars[0], []).extend(pending)
        pending = []
if pending:                                   # trailing specials: attach to the last paragraph
    specials.setdefault(ids[-1], []).extend(pending)

printed = set()   # a block shared by several paragraphs is shown once
for p in la:
    if p['id'] not in wanted:
        continue
    for folio, it in specials.get(p['id'], []):
        print(f'\n=== SPECIAL BLOCK {it["pair"]} (folio {folio}): translate whole, key "{it["pair"]}"')
        for part in it['la']:
            print('LATIN:', part.get('raw') or part.get('pre'))
        if show_zh:
            print('CHINESE EDITION:', zh.get(it['pair'], ''))
    print(f'\n=== PARAGRAPH {p["id"]}')
    for k, t in p['s'].items():
        print(f'{p["id"]}.{k}: {t}')
    if show_zh:
        for bk in blocks_of.get(p['id'], []):
            if bk in printed:
                continue
            printed.add(bk)
            print(f'  [Chinese edition, block {bk}]: {zh.get(bk, "")}')
