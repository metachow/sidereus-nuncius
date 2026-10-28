# 任务 E：f24r–f28v（扫描 0055–0064）

## 完成情况
- f24r f24v f25r f25v f26r f26v f27r f27v f28r f28v 共 10 叶，`check_folio` 全部 OK，逐页看过 PNG。
- f28v 起初溢出两行，删掉第三条脚注（元素天球）并压缩了几处中文措辞（信息未删）后 OK。

## 衔接
- f24r 拉丁文第一个词：**orientales**（`\noindent orientales, et una occidentalis, in tali dispositione:`），与 f23v 末词 duae 衔接（f23v 页脚提示词 orien- 不录）。
- f24r 中文第一句：“最东的那颗相当小，与下一颗相距四角分；……”（二月九日那句整句已在 f23v）。f24r 第一个 `\ZH` 为空（只有注释），f28r 同样（Hasce … collationes apponere placuit 一句整句译在 f27v）。
- 页内跨页单词按规范整词归前页：occi-|dentalibus（24v）、a-|berat（25r）、col-|lationes（27v）、va-|gantes（28r）。

## 插图
- 共 29 幅木星图，全部用 `\jove`；坐标为 jove_measure 结果加手工核对（另写脚本列出连通域逐颗量）。
- 删掉的误检：II.9 的 −8.6（Ori.）；II.11 h.3 的 4.5（Occ.）；II.13 的 [−2.2/−0.41]（背面透印的木星环）；II.16 的 −5.0（污点）；II.21 的 2.5、II.15 h.6 的 −1.25 与 2.0、III.1 的 −3.9（初版图中竖线／括号状的铅字杂痕，不是星）；II.28 h.5 的 6.1（Occ.）。
- 手工补上的星：II.10 的 −0.8、II.11 h.3 的 −0.85、II.12 的 −0.65、II.15 h.1 拆分出的两颗近星（−1.25、−0.9）、II.15 h.5/h.6 的 −0.72/−0.75、II.15 h.6 的西星 1.4、II.26 h.5 两幅图里的 0.7、II.27 的 −0.75。
- 星的大小按字模高度换算（普通星约 0.6 个木星直径 = 1）。
- 文中说“偏北”而图上也看得出的：III.1 第三颗（dy 0.23）、III.2 最东一颗（dy 0.15），放进离线列表。II.11 h.3 第四颗，文字说 modicum in aquilonem deflectens，但初版图上看不出偏离，按图放在线上。
- **恒星（fixa）图**：II.26 h.5（第二幅）、II.27、II.28 h.1、III.1、III.2 这五幅是木星图加一颗下方注有 “fixa” 的恒星。我没有用占位框，而是用 `\jove` 画出，把恒星作为离线星（dy −2.1 到 −3.75），“fixa”写进标签：`（下方之星：fixa，恒星）`；图后加了 `\par\vspace{1.5mm}` 留空隙。II.26 那幅初版没有 Occ.，`\jove` 照常印出。
- 标签：同一夜多幅图才加时刻，II.11 h.5½ 写作 `h.\,5, m.\,30`，II.26 第一幅写作 `h.\,0, m.\,30`（同 D 的格式）。
- 图的移动：初版图常夹在句中或词中。做法是移到其后第一个句号或冒号处（Favaro 标点）；若会跨页（II.11 h.3），放在本页末尾；若图只是把句首一个词断开（II.9 O-|rientalior、II.27 Vici-|niores），放在该句之前。II.16、II.18 h.6 的图在初版中位于下一页，故放在 25v、26r。

## 拉丁文异文
- 25v `distans`：初版 distas（误排），已加注释。
- 26v `ac min. 4`：维基文库本作 “ac. min. 4”，从初版。
- 27v `sec. 20`：初版作 20，维基文库本作 “sec. 2”，从初版（加了注释）。**请核对 Favaro 印本。**
- 28r `duodecennales`：初版 “duo decẽnales”；`hauriuntur`：初版 auriuntur（均加注释）。
- 28v `planetae \textsc{medicei}`：初版误作 MEDICEA，从 Favaro（加注释）。
- “veluti in figura. Sed, hora 5”（27r）、“ut in figura.”（27v）：Favaro 在这两处用冒号引出图，因图已移位，改用初版的句号。
- 拼写：Eclypticae→eclipticae，coelum→caelum，quatuor→quattuor，nunquam→numquam，tanquam→tamquam，plerunque→plerumque，intelligere→intellegere，expectet→exspectet，Depraehenditur→deprehenditur，orizontem→horizontem，Sistemate→systemate，aër→aer；`m.`／`Ho.` 一律写作 `min.`／`hora`。`pronunciare`、`arcta`、`lubens` 照 Favaro 保留。普通名词小写（stella, planeta, fixa, zodiacus, ecliptica, aquilo, auster, boreas, luminaria, lector, systema）；`a Terra elongari` 按规范大写 Terra。

## 译法（新增或需统一）
- 时刻、角度与 D（f18v–f23v）统一：序数词的 hora tertia → 第三个小时；数字 hora 1, min. 30 → 一时三十分（不加“入夜后”）；min. 2 → 两角分。例外：hora quinta cum dimidia → “五时半”（“第五个半小时”有歧义）。
- Medicei planetae → 美第奇行星；Medicea Sidera → 美第奇星；fixa → 恒星；collatio ad fixam → 与恒星的比较；tabulae → 天文表（加了脚注）；ovalis motus → 卵形运动；luminaria → 日月两大发光体；elementorum sphaera → 元素天球；candidus lector → 坦诚的读者；in nostro systemate → 在《体系》中（加了脚注：伽利略计划写的宇宙体系著作）。
- 脚注：27v（天文表）、28r（木卫四实际周期约 16.7 天）、28v（《体系》）。

## 需要主编决定
1. 五幅恒星图：用 `\jove` 加离线星的画法是否可以，还是改用占位框或重绘（以便在恒星旁标出 “fixa”）。
2. 27v 的 sec. 20 和 sec. 2：请核对 Favaro 印本。
3. 图的移动规则（见上）是否需要与其他叶统一。
4. 是否把 `pronunciare` 改作 `pronuntiare`，把 `arcta` 改作 `arta`。
