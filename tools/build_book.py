"""Build the whole book and check it.

usage: python tools/build_book.py [--lang en]

Regenerates folia/ (or folia_<lang>/) from text/, runs xelatex twice on main.tex
(or main_<lang>.tex), then checks that the recto folia fall on odd (right-hand)
pages and reports LaTeX errors and overfull boxes.
"""
import os
import re
import subprocess
import sys

import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_folia import build  # noqa: E402

lang = sys.argv[sys.argv.index('--lang') + 1] if '--lang' in sys.argv else 'zh'
main = 'main' if lang == 'zh' else f'main_{lang}'
build(lang, 'folia' if lang == 'zh' else f'folia_{lang}')

for _ in range(2):
    r = subprocess.run(['xelatex', '-interaction=nonstopmode', main + '.tex'],
                       cwd=ROOT, capture_output=True)
log = open(os.path.join(ROOT, main + '.log'), encoding='utf-8', errors='replace').read()
errors = re.findall(r'^! .*', log, re.M)
overfull = re.findall(r'^Overfull .*', log, re.M)
doc = fitz.open(os.path.join(ROOT, main + '.pdf'))
bad = []
for i, page in enumerate(doc):
    m = re.search(r'\[\s*(\d+)\s*([a-z]?)\s*(?:\\,)?\s*([rv])\s*\]', page.get_text())
    if m and (m.group(3) == 'r') != ((i + 1) % 2 == 1):
        bad.append(i + 1)
print(f'{len(doc)} pages; errors: {len(errors)}; overfull boxes: {len(overfull)}; '
      f'recto/verso parity errors: {bad or "none"}')
for e in errors:
    print('  ', e)
sys.exit(1 if errors or bad else 0)
