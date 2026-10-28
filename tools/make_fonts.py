"""Export static weights of Noto Serif SC into fonts/.

usage: python tools/make_fonts.py [PATH_TO_NotoSerifSC-VF.ttf]

XeTeX loads only the default instance of a variable font (ExtraLight for Noto
Serif SC), so the book uses static Regular / SemiBold / Bold files cut from the
variable font with fontTools. Noto Serif SC is under the SIL Open Font License.
Default path: the Windows system copy. The variable font is also available from
https://github.com/notofonts/noto-cjk (Serif/Variable/TTF).
"""
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1] if len(sys.argv) > 1 else 'C:/Windows/Fonts/NotoSerifSC-VF.ttf'
os.makedirs(os.path.join(ROOT, 'fonts'), exist_ok=True)
for name, w in (('Regular', 400), ('SemiBold', 600), ('Bold', 700)):
    font = instancer.instantiateVariableFont(TTFont(src), {'wght': w}, updateFontNames=True)
    font.save(os.path.join(ROOT, 'fonts', f'NotoSerifSC-{name}.ttf'))
    print(name)
