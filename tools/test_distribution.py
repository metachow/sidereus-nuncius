"""Test sentence-level distribution: use the Latin as a stand-in translation and check
that every sentence lands exactly once, on the page where its Latin sentence starts.

usage: python tools/test_distribution.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, 'tools')
from textmodel import dump_yaml, load_yaml, segments  # noqa: E402

la = load_yaml('text/la.yaml')
test = {f"{p['id']}.{k}": f"<<{p['id']}.{k}>>" for p in la for k in p['s']}
dump_yaml(test, 'text/xx.yaml')
subprocess.run([sys.executable, 'tools/gen_folia.py', '--lang', 'xx', '--out', 'build/folia_xx'], check=True)
os.remove('text/xx.yaml')

# expected page of each sentence: folio of the segment it starts in
layout = load_yaml('text/layout.yaml')
seg_page = {}
for page in layout:
    for it in page.get('items', []):
        for part in it.get('la', []):
            if 'seg' in part:
                seg_page[part['seg']] = page['file']
expected = {}
for p in la:
    _, start = segments(p)
    for k, s in start.items():
        expected[f"{p['id']}.{k}"] = seg_page[f"{p['id']}:{s}"]

found = {}
for f in os.listdir('build/folia_xx'):
    if f == 'order.tex':
        continue
    text = open('build/folia_xx/' + f, encoding='utf-8').read()
    zh_parts = text.split('\\ZH')[1:]
    for part in zh_parts:
        for key in re.findall(r'<<(p\d+\.\d+)>>', part.split('\\LA')[0]):
            found.setdefault(key, []).append(f[:-4])
missing = [k for k in test if k not in found]
dups = [k for k, v in found.items() if len(v) > 1]
wrong = [k for k, v in found.items() if v[0] != expected[k]]
print(f'{len(found)} of {len(test)} sentences placed; missing {missing}; duplicated {dups}; on wrong page {wrong}')
