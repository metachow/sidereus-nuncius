"""Fit overflowing pages of a translation edition onto one page by tightening the
translation column of that page only, in small steps, lightest first.
Steps per edition (STEPS below): English normal 10.2/14.6, Japanese 9.4/15.6.

usage: python tools/fit_pages.py --lang en f05r f11r ...

For each folio, tries the sizes in STEPS[lang] (font size, leading in pt) until tools/check_folio.py reports one page, and
records the result as tr_size in text/layout.yaml. A page that still overflows
at the last step is reported for manual work (shorter note, smaller figure).
"""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_folia import build  # noqa: E402
from textmodel import dump_yaml, load_yaml  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# (Latin column, translation column); None = unchanged (10.2/14.6). Paracol aligns
# every pair, so when the last translation block is what runs over, only a tighter
# Latin column moves its starting point up.
STEPS = {
    'en': [(None, (10.2, 14.2)), (None, (10.2, 13.9)), (None, (10.2, 13.6)), (None, (10.0, 13.4)),
           ((10.2, 14.2), (10.0, 13.4)), ((10.2, 13.9), (10.0, 13.4)), ((10.2, 13.6), (9.8, 13.2)),
           ((10.0, 13.4), (9.8, 13.2)), ((9.8, 13.2), (9.6, 12.9))],
    # Japanese column: normal 9.4/15.6
    'ja': [(None, (9.4, 15.0)), (None, (9.4, 14.5)), (None, (9.2, 14.2)), (None, (9.0, 13.8)),
           ((10.2, 14.2), (9.0, 13.8)), ((10.2, 13.9), (9.0, 13.6)), ((10.0, 13.4), (8.8, 13.4)),
           ((9.8, 13.2), (8.8, 13.2))],
}

args = sys.argv[1:]
i = args.index('--lang')
lang = args[i + 1]
folios = args[:i] + args[i + 2:]
path = os.path.join(ROOT, 'text', 'layout.yaml')
header = ''.join(l for l in open(path, encoding='utf-8') if l.startswith('#'))


def fits(name):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'check_folio.py'),
                        '--lang', lang, name], cwd=ROOT, capture_output=True, text=True)
    return r.returncode == 0


for name in folios:
    layout = load_yaml(path)
    page = next(p for p in layout if p['file'] == name)
    done = None
    for la_size, tr_size in STEPS[lang]:
        page.setdefault('tr_size', {})[lang] = list(tr_size)
        if la_size:
            page.setdefault('la_size', {})[lang] = list(la_size)
        else:
            page.get('la_size', {}).pop(lang, None)
            if 'la_size' in page and not page['la_size']:
                del page['la_size']
        dump_yaml(layout, path, header)
        build(lang, f'folia_{lang}')
        if fits(name):
            done = (la_size, tr_size)
            break
    if done:
        la = f'Latin {done[0][0]}/{done[0][1]}, ' if done[0] else ''
        print(f'{name}: fits at {la}translation {done[1][0]}/{done[1][1]} pt')
    else:
        print(f'{name}: STILL TOO LONG at the last step; needs manual work')
