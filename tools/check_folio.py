"""Compile one folio on its own and check that it fits on exactly one page.

usage: python tools/check_folio.py f08v [f09r ...]
Run from anywhere; output goes to build/. Each folio gets its own job name,
so several folios can be checked in parallel without clobbering each other.
Prints page count, LaTeX errors and overfull boxes, and renders
build/check_<name>.png (80 dpi) for a visual check.
"""
import os
import re
import subprocess
import sys

import fitz

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check(name):
    os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
    job = f'check_{name}'
    start = 2 if name.endswith('v') else 1      # versos fall on even pages
    tex = rf'\def\onlyfolio{{{name}}}\def\startpage{{{start}}}\input{{main}}'
    cmd = ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
           '-output-directory=build', f'-jobname={job}', tex]
    for _ in range(2):                           # second run settles footnotes
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True)
    log = open(os.path.join(ROOT, 'build', job + '.log'), encoding='utf-8', errors='replace').read()
    errors = re.findall(r'^! .*', log, re.M)
    overfull = re.findall(r'^Overfull .*', log, re.M)
    pdf = os.path.join(ROOT, 'build', job + '.pdf')
    if r.returncode != 0 or not os.path.exists(pdf):
        print(f'{name}: FAILED')
        for e in errors:
            print('   ', e)
        return False
    doc = fitz.open(pdf)
    n = len(doc)
    png = os.path.join(ROOT, 'build', job + '.png')
    doc[0].get_pixmap(dpi=80).save(png)
    status = 'OK' if n == 1 else f'TOO LONG ({n} pages)'
    print(f'{name}: {status}; image: {png}')
    for o in overfull:
        print('    ', o)
    return n == 1


if __name__ == '__main__':
    ok = all([check(a.replace('.tex', '').replace('folia/', '')) for a in sys.argv[1:]])
    sys.exit(0 if ok else 1)
