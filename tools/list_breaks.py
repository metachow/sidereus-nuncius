"""List the sentences that run across a page of the 1610 edition, with the Latin
(marker in place), the current translation and the file it is in.

usage: python tools/list_breaks.py en
Put the same marker (e.g. ⟦8v⟧) into the translation at the matching point and the
generator splits the translated sentence across the two pages like the Latin.
Sentences without a marker in the translation go whole to the earlier page.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textmodel import load_yaml  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
lang = sys.argv[1]
la = load_yaml(os.path.join(ROOT, 'text', 'la.yaml'))
where = {}
d = os.path.join(ROOT, 'text', lang)
for fn in sorted(os.listdir(d)):
    if fn.endswith('.yaml'):
        for k, v in (load_yaml(os.path.join(d, fn)) or {}).items():
            where[k] = (fn, v)
n = done = 0
for p in la:
    for s, t in p['s'].items():
        marks = re.findall(r'⟦[^⟧|]+⟧', t)
        if not marks:
            continue
        key = f'{p["id"]}.{s}'
        fn, tr = where.get(key, ('-', ''))
        has = len(re.findall(r'⟦[^⟧]*⟧', tr)) == len(marks)
        n += 1
        done += has
        print(f'\n=== {key} in text/{lang}/{fn}  markers {" ".join(marks)}  {"[done]" if has else ""}')
        print('LATIN:', t)
        print('TRANSLATION:', tr)
print(f'\n{n} sentences cross a page; {done} already marked')
