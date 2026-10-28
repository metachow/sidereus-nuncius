"""Export static weights of Noto Serif SC (and JP, for the Japanese edition) into fonts/.

usage: python tools/make_fonts.py [PATH_TO_NotoSerifSC-VF.ttf] [--ja [PATH_TO_NotoSerifJP-VF.ttf]]

XeTeX loads only the default instance of a variable font (ExtraLight for Noto
Serif SC), so the book uses static Regular / SemiBold / Bold files cut from the
variable font with fontTools. Noto Serif SC is under the SIL Open Font License.
Default path: the Windows system copy. The variable font is also available from
https://github.com/notofonts/noto-cjk (Serif/Variable/TTF). --ja cuts Noto Serif JP
the same way (only the Japanese edition needs it).
"""
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
args = sys.argv[1:]
jobs = []
if '--ja' in args:
    i = args.index('--ja')
    ja = args[i + 1] if i + 1 < len(args) and not args[i + 1].startswith('--') else None
    jobs.append(('NotoSerifJP', ja or 'C:/Windows/Fonts/NotoSerifJP-VF.ttf'))
    del args[i:i + (2 if ja else 1)]
    if args:
        jobs.insert(0, ('NotoSerifSC', args[0]))
else:
    jobs.append(('NotoSerifSC', args[0] if args else 'C:/Windows/Fonts/NotoSerifSC-VF.ttf'))
os.makedirs(os.path.join(ROOT, 'fonts'), exist_ok=True)
for family, src in jobs:
    for name, w in (('Regular', 400), ('SemiBold', 600), ('Bold', 700)):
        font = instancer.instantiateVariableFont(TTFont(src), {'wght': w}, updateFontNames=True)
        font.save(os.path.join(ROOT, 'fonts', f'{family}-{name}.ttf'))
        print(family, name)
