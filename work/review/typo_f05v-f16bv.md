# 字体角色标注记录：f05v–f16bv

范围：f05v、f06r、f06v、f07r–f16v、f16ar、f16av、f16br、f16bv（扫描 0014–0040），共 26 页。
方法：逐页看 `work/pages/NNNN.png`；凡拿不准的地方（f06r 首字母、f16ar 图题、f16br 段首 Q）用 `scans/NNNN.png` 裁局部放大核对。
修改前的副本：scratchpad `backup/`。

## 1. 结论

**本范围内初版没有用意大利斜体排的文字。** 26 页的正文、图题、图中字母全是正体（roman）。初版的斜体只在书名页、献词这类前置部分出现（对照看过 0013 的书名页斜体，字形差别非常明显，不会看漏）。所以本范围没有加 `\lital` / `\zhital`。

**大写强调**都集中在星图那几页，拉丁文原来已经全部标好，与初版逐一核对一致，没有多标也没有漏标：

| 叶 | 扫描 | 初版 | 拉丁文 | 中文 |
|---|---|---|---|---|
| f16ar | 0037 | PLEIADAS（正文） | `\capsemph{Pleiadas}` ✓ | `\zhemph{昴星团}` ✓ |
| f16ar | 0037 | 图题 Cinguli, & Ensis ORIONIS Asterismus.（只有 ORIONIS 大写，其余正体） | ✓ | `\zhemph{猎户座}` ✓ |
| f16br | 0039 | 图题 PLEIADVM CONSTELLATIO. | ✓ | **补**：`\zhemph{昴星团}`（原为普通字体） |
| f16br | 0039 | LACTEI Circuli（只有 LACTEI 大写） | ✓ | `\zhemph{银河}` ✓（Lactei Circuli 整体译“银河”） |
| f16br | 0039 | GALAXYA ×2 | ✓ | ✓ |
| f16bv | 0040 | NEBVLOSAE | ✓ | `\zhemph{星云状}` ✓ |
| f16bv | 0040 | NEBVLOSAM Capitis Orionis（只有 NEBVLOSAM 大写） | ✓ | **改**：`\zhemph{猎户头部星云}` → `猎户头部\zhemph{星云}` |
| f16bv | 0040 | NEBVLOSAM PRAESEPE | ✓ | ✓ |
| f16bv | 0040 | 图题 NEBVLOSA ORIONIS. / NEBVLOSA PRAESEPE. | ✓ | **补**：`\zhemph{猎户头部星云}`、`\zhemph{鬼星团}` |

合计：大写强调 12 处（正文 7、图题 5），全部已标；本次只改中文 3 处（f16br 1、f16bv 2），拉丁文未动。斜体 0 处。

f05v–f16v 正文里首字母大写的词（Nebulosas、Stellas、Perspicillum、Organum、Refractionibus、Systemate Mundi 等）只是首字母大写，不是强调，没有标。

## 2. check_folio

26 页全部 **OK**（各一页）。改过的 f16br、f16bv 看过 PNG，版面正常；中文粗体没有引起溢出。

## 3. 木刻装饰清单（主编裁图用）

**本范围内没有木刻装饰**：没有装饰首字母，没有页首花饰带，也没有尾花。逐页看过的情况：

| 叶 | 扫描 | 情况 |
|---|---|---|
| f06r | 0015 | 第二段 “MENSIBVS abhinc decem…” 段首有一个**两行高的大写字母 M**（版心左上，第 3–4 行）。放大看是素面的正体铅字大写，黑实笔画，**没有花纹底框，不是木刻装饰首字母**。位置：`work/pages/0015.png` 约 x 206–300、y 280–355；`scans/0015.png` 约 x 630–920、y 860–1085。后接 ENSIBVS 为同行的正体大写字母。 |
| f16br | 0039 | 段首 “Quòd” 的 Q 是普通正文字号，只是印得很淡，不是首字母装饰。 |
| 其余各页 | 0014–0040 | 无装饰。0019、0022、0023、0024 的月面图是铜版画（不是木刻装饰），0037–0040 的星图是另版印的图，都已有占位符，不在本清单内。 |

（初版的页首花饰带见 0013 = f05r，属主编范围。）

## 4. 疑问，请主编决定

1. **f06r 的 MENSIBVS**：初版这里是“两行大写首字母 M + 同行其余字母大写”的开篇格式，是排版惯例，不是对词义的强调，所以我**没有**用 `\capsemph`，拉丁文仍作 `Mensibus`。若要在本版再现这一开篇格式（例如首字母下沉加 `\dispcaps`），需要 preamble 增加相应宏，由主编统一处理（f17r 的 “De Luna” 段在初版没有这种格式，可不管）。
2. **书名斜体**：f15r `\textit{De systemate mundi}`、f16r `\textit{Systemate mundi}` 在初版是**正体**（0033 第 6 行 “de Sistemate mundi”、0035 第 3 行 “Systemate Mundi”）。这里的斜体是按 DECISIONS C 组第 6 条加的编辑斜体，不是初版字体，所以保留 `\textit`，**没有**改成 `\lital`，以免把编辑体例当成初版字体。若主编希望全书只用角色宏，可改为 `\lital`，排出来效果相同。
3. f16br 的 Lactei Circuli 初版只把 LACTEI 排成大写，中文“银河”是 Lactei Circuli 两个词合译，无法只加粗其中一部分，所以整体加粗，保持现状。
