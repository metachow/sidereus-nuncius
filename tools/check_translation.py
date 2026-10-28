"""Check one translator's file: completeness, LaTeX sanity, and that its pages compile.

usage: python tools/check_translation.py en text/en/part1.yaml p001 p014

1. the file parses; every sentence p001.01 ... p014.NN and every special block in
   the range has an entry (no extras outside the range, no empty entries)
2. no leftover markers (⟦…⟧), no Chinese characters, balanced braces
3. generates the English pages into build/folia_en_<part>/ and compiles each
   folio of the range on its own; LaTeX errors are reported. Pages that run
   long are listed for information only: page fitting is done later.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_folia import build  # noqa: E402
from textmodel import load_yaml  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lang, path, a, b = sys.argv[1:5]
tag = os.path.splitext(os.path.basename(path))[0]
data = load_yaml(os.path.join(ROOT, path)) or {}
la = load_yaml(os.path.join(ROOT, 'text', 'la.yaml'))
layout = load_yaml(os.path.join(ROOT, 'text', 'layout.yaml'))
ids = [p['id'] for p in la]
wanted = ids[ids.index(a):ids.index(b) + 1]

# expected keys: sentences of the range + special blocks attached to it
expected = [f'{p["id"]}.{k}' for p in la if p['id'] in wanted for k in p['s']]
folios, pending = [], []
for page in layout:
    for it in page.get('items', []):
        if 'pair' not in it:
            continue
        pars = [part['seg'].split(':')[0] for part in it['la'] if 'seg' in part]
        if not pars:
            pending.append((page['file'], it['pair']))
            continue
        if pars[0] in wanted or (pending and pars[0] in wanted):
            for f, k in pending:
                if pars[0] in wanted:
                    expected.append(k)
                    folios.append(f)
        pending = []
        if any(p in wanted for p in pars):
            folios.append(page['file'])
if pending and ids[-1] in wanted:
    for f, k in pending:
        expected.append(k)
        folios.append(f)
folios = list(dict.fromkeys(folios))

problems = []
missing = [k for k in expected if k not in data]
extra = [k for k in data if k not in expected]
empty = [k for k, v in data.items() if not str(v).strip()]
if missing:
    problems.append(f'missing {len(missing)}: {missing[:12]}')
if extra:
    problems.append(f'not in this range: {extra[:12]}')
if empty:
    problems.append(f'empty: {empty[:12]}')
for k, v in data.items():
    v = str(v)
    if '⟦' in v:
        problems.append(f'{k}: contains a page marker ⟦…⟧')
    if re.search(r'[一-鿿]', v):
        problems.append(f'{k}: contains Chinese characters')
    depth = 0
    for i, c in enumerate(v):
        if c == '{' and (i == 0 or v[i - 1] != '\\'):
            depth += 1
        elif c == '}' and (i == 0 or v[i - 1] != '\\'):
            depth -= 1
        if depth < 0:
            break
    if depth != 0:
        problems.append(f'{k}: unbalanced braces')

out = f'build/folia_{lang}_{tag}'
build(lang, out)
long_pages = []
for f in folios:
    job = f'check_{lang}_{tag}_{f}'
    start = 2 if f.endswith('v') else 1
    tex = (rf'\def\foliadir{{{out}}}\def\onlyfolio{{{f}}}'
           rf'\def\startpage{{{start}}}\input{{main_{lang}}}')
    r = subprocess.run(['xelatex', '-interaction=nonstopmode', '-halt-on-error',
                        '-output-directory=build', f'-jobname={job}', tex],
                       cwd=ROOT, capture_output=True)
    log = open(os.path.join(ROOT, 'build', job + '.log'), encoding='utf-8', errors='replace').read()
    errs = re.findall(r'^! .*', log, re.M)
    if r.returncode != 0 or errs:
        problems.append(f'{f}: LaTeX error {errs[:2]}')
    else:
        m = re.search(r'Output written on .*\((\d+) page', log)
        if m and int(m.group(1)) > 1:
            long_pages.append(f)

print(f'{len(expected)} entries expected, {len(data)} present; folios {folios[0]}–{folios[-1]}')
print('pages running long (for information):', long_pages or 'none')
print('PROBLEMS:' if problems else 'OK, no problems.')
for p in problems:
    print('  ', p)
sys.exit(1 if problems else 0)
