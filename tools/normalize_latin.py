"""Apply the orthography decisions in work/DECISIONS.md across all folia.

Only the part of each line before a LaTeX comment (%) is changed.
usage: python tools/normalize_latin.py folia [--apply]   (dry run without --apply)
"""
import os
import re
import sys

folia, apply = sys.argv[1], '--apply' in sys.argv

ORD = r'(prim|secund|terti|quart|quint|sext|septim|octav|non)'
rules = [
    # ex + s: exsisto, but not existimo ("to think")
    (re.compile(r'\b([Ee])xist(?!im)'), r'\1xsist'),
    # compound ordinals and numerals written apart
    (re.compile(r'\b(decim|vicesim|vigesim)(a|ae|am)' + ORD + r'(a|ae|am)\b'), r'\1\2 \3\4'),
    (re.compile(r'\bvigintiun(as|ae|a)\b'), r'viginti un\1'),
    (re.compile(r'\btrigintasex\b'), r'triginta sex'),
    # classical spellings
    (re.compile(r'\b([Vv])igesim'), r'\1icesim'),
    (re.compile(r'\b([Tt])rigesim'), r'\1ricesim'),
    (re.compile(r'\bmilliar'), r'miliar'),
    (re.compile(r'\barct(a|us|um|ae|is|o)\b'), r'art\1'),
    # units: seconds as "sec.", minutes as "min."
    (re.compile(r'\bmin\. sec\.'), r'sec.'),
    (re.compile(r'\b(min\. pr\.|min\. p\.|m\. p\.)'), r'min.'),
    (re.compile(r'(?<![a-z])pr\. (\d)'), r'min. \1'),
    # cross references in Chinese footnotes: 第 6 叶正面 -> [6r]
    (re.compile(r'第\s*(\d+)\s*叶\s*正面'), r'[\1r]'),
    (re.compile(r'第\s*(\d+)\s*叶\s*背面'), r'[\1v]'),
]


def split_comment(line):
    m = re.search(r'(?<!\\)%', line)
    return (line[:m.start()], line[m.start():]) if m else (line, '')


total = 0
for fn in sorted(os.listdir(folia)):
    if not fn.endswith('.tex') or fn == 'order.tex':
        continue
    path = os.path.join(folia, fn)
    lines = open(path, encoding='utf-8').read().split('\n')
    changed = False
    for i, line in enumerate(lines):
        body, comment = split_comment(line)
        new = body
        for pat, rep in rules:
            for m in pat.finditer(new):
                print(f'{fn}:{i+1}: {m.group(0)!r} -> {pat.sub(rep, m.group(0))!r}')
                total += 1
            new = pat.sub(rep, new)
        if new != body:
            lines[i] = new + comment
            changed = True
    if changed and apply:
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
print('changes:', total, '(applied)' if apply else '(dry run)')
