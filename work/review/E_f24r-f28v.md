# 校对记录：E 组 f24r–f28v（扫描 0055–0064）

校对范围 10 叶，改完后 `check_folio` 全部 **OK**（各一页、无 overfull），PNG 逐页看过。

## 通查结果（各页共同）

- **断页**：10 叶的拉丁文起止都与初版一致。跨页单词整词归前页（occi-|dentalibus 24v、a-|berat 25r、col-|lationes 27v、va-|gantes 28r）；提示词（minor、dentali-、berat、Ioue、æquales、min. 2.、omnes、latio-、gantes）和帖号（G、G 2）都没有录入。
- **拉丁文逐句对照扫描和维基文库 Favaro 本**：没有发现漏词、多词或词序错误；时刻、角分、角秒全部与初版一致。原有的异文注释（distas、ac. min. 4、sec. 20、auriuntur、duo decẽnales、MEDICEA）核对无误。
- **衔接**：f23v（未改动）以 `adstabant Iovi stellae duae` 和中文“……排列如下：”结尾；f24r 以 `orientales, et una occidentalis, in tali dispositione:` 开头，中文从二月九日图后的一句开始，没有重复也没有遗漏。f28v 以 `… candidus lector exspectet.` 和 FINIS 收尾，中文以“完”收尾，与初版相同。
- **木星图**：29 幅全部用 `jove_measure.py` 复测，并放大扫描逐幅核对。星的数目、东西位置、偏离直线的方向都正确，原记录里删去的误检（Ori./Occ. 字样、污点、铅字杂痕）也确认无误。只改了星的大小，按规范和 C 组校对第 2 条统一为简单值：文字说较大或明显较亮的星取 1.3，普通星取 1，较小的取 0.8，极小的取 0.6。
- **术语统一（与 f18v–f23v 一致）**：hora tertia → 第三个小时；hora 1, min. 30 → 一时三十分；min. 2 → 两角分。`secundum eclipticae ductum` 原来有“沿黄道方向”“沿黄道的走向”两种译法，统一为“沿黄道的走向”，与 D 组的 zodiaci ductum →“沿黄道带的走向”对应。
- **插图位置**（执行 D-1、E-3）：图一律移到引出它的分句之后，也就是被图打断的那个句子开始之前；有明确的 “ut/veluti in figura”“in tali configuratione” 时放在那里（同 Favaro），两栏同步。引出图的分句在上一页、图本身在下一页的，图留在本页，放在本页第一句之后（II.16、II.18 h.6、II.27），图旁加了注释。

## 各页改动

- **f24r**：II.11 h.1 移到 “et una ab occasu.”／“西侧有一颗。”之后，距离那句随图移到图后。II.9 的大小改为 0.8／1.3／0.8；II.11 h.3 的近星改为 0.6。II.11 h.3 按 E-3 留在页尾。
- **f24v**：II.12 移到 “adstabant.” 之后，II.13 移到 “duae insuper ab occasu.” 之后，两栏的段落相应调整。`decimatertia` → `decima tertia`（C 组校对第 3 条，加 `% 1610:` 注释）。中文“稍稍偏离……略向北偏”语义重复，改为“稍向北偏离穿过其余各星所引的直线”。改了几颗星的大小。
- **f25r**：II.15 h.1 移到 “talis fuit astrorum positus:” 之后（同 Favaro），“tres nempe … occidentalis:” 随之移到图后。`decimaquinta`、`decimaquarta`、`decimasexta` 分写，加注释。“更靠近西边那颗”改为“离西边那颗较近”。改了几颗星的大小（II.15 h.1 最东一颗“reliquis maior”取 1.3）。
- **f25v**：II.17 移到 “duae aderant stellae:” 之后，II.18 h.1 移到 “orientalis vero una:” 之后。`decimaseptima` 分写。distas 注释写明指的是第二个 distans。II.16 留在本页第一句之后，加了注释。
- **f26r**：II.21 移到 “in hac constitutione:” 之后。II.19 两颗星（“satis magnae”）取 1.3，II.21 三颗取 0.8，II.18 h.6 的近星取 0.8。改“沿黄道的走向”。II.19 被图打断的那一整句就是引出它的句子，所以图仍放在句末。
- **f26v**：II.26 h.0 m.30 移到 “binae tantum aderant stellae:” 之后，II.26 h.5（第一幅）移到 “tres visae sunt stellae:” 之后。带恒星的那幅图把恒星移到 `\jove` 的第四个参数，去掉了原来手写的“（下方之星：fixa，恒星）”标签和 `\vspace`。改“沿黄道的走向”。
- **f27r**：II.27 的恒星移到第四个参数，西端星取 1.3（“in primis occidua”）。II.28 h.1 的恒星移到第四个参数，图从 “in eadem recta:” 之后移到 “veluti in figura:” 之后（同 Favaro），后面恢复 Favaro 的冒号和小写 `sed`。改“沿黄道的走向”。
- **f27v**：III.1 图移到 “ut in figura:” 之后（同 Favaro），III.2 图移到 “in tali configuratione:” 之后，图后恢复 Favaro 的大写 `Aberat`。两幅图的恒星移到第四个参数；III.1 偏北的星和 III.2 偏北的最东星仍放在第三个参数。大小按文字调整：III.1 最东一颗“reliquis minor”取 0.6；III.2 两端（“lucidiores ac maiores”）取 1.3。
  - **sec. 20 / sec. 2**：放大扫描 0062 第二行，初版清楚地印作 “tertia m. 0. ſec. 20.”。维基文库录的 Favaro 本作 “sec. 2”，可能是录入时漏掉了 0，也可能 Favaro 印本本来就这样，手头没有纸本无法判断。正文从初版作 `sec. 20`，译“二十角秒”，行末注释已写明。
- **f28r**：没有改动（拉丁文、中文和脚注核对无误）。
- **f28v**：`arcta` → `arta`（E-4）；中文“紧凑的圆周运动”改为“狭小的圆周运动”，更贴合 arta 的意思。

## 仍需主编决定

1. **f27v sec. 20**：请用 Favaro 国家版纸本（第三卷）核对它是否本作 “sec. 2”。若是，可考虑加一条脚注说明异文。
2. **引出分句在前一页的三幅图**（II.16、II.18 h.6、II.27）：现在放在本页第一句之后（II.27 恰好也是初版的位置）。另一种做法是 II.27 放在本页的 “ut in apposita figura videre licet.” 之后。请确认。
3. **II.26 h.5 的两幅图标签相同**（`II. 26, h. 5`），因为初版第二幅只是加了恒星。是否给第二幅另加区分，比如“（与恒星比较）”？
4. **合写的序数词**：本范围已按 C 组校对第 3 条分写为 decima tertia／quinta／quarta／sexta／septima。f18v 仍有合写形式（不在本范围），需要全局统一。
5. **“五时半”**（24v，hora quinta cum dimidia）：沿用 E 的处理，没有按序数译作“第五个小时……半”。请确认。
