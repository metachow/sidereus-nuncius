# 校对记录：f17v–f23v（扫描 0042–0054）

范围：f17v、f18r（主编样张），f18v、f19r、f19v、f20r、f20v、f21r、f21v、f22r、f22v、f23r、f23v。
13 叶改完后全部重新运行 `check_folio`，结果均为 **OK**（每叶一页），PNG 已查看。

## 全范围统一执行（DECISIONS「来自 D 组」）

- `vigesima` → `vicesima`，合写形式一并改（vicesimaprima、vicesimaquarta、vicesimaquinta）：f20r、f20v、f21r、f21v、f22r。
- 单位缩写：`min. pr.`、`m. p.`、`min. p.` 一律改作 `min.`（f19r、f19v×2、f20v×3、f21r、f21v×2）。`min. sc. vix 30`（f19r）改作 `min. sec. vix 30`，与初版本来就有的 `min. sec. 20`（f22v）、`min. tantum sec. 20`（f19v）一致，这样全范围只用 min.、sec. 两种缩写。
- 插图位置：逐幅核对过，都在引出它的分句之后。II.2 h.7（f22v）按 Favaro 改到 “quattuor aderant stellae:” 之后，“inter quas Iuppiter mediam occupabat sedem” 移到图后，中文同步（“出现了四颗星：”／图／“木星位于它们中间。”）。I.26 h.5 原来就在 “ut apposita figura demonstrat:” 之后，与 Favaro 一致，没有改。
- 句子没说完、只能留在页尾的三幅图（I.24 h.6 在 f21r，I.31 h.4 在 f22r，II.6 在 f23r）：按规范第 2.5 条各加了一行注释说明。
- f21r（1 月 24 日第六个小时）：加脚注，说明文字有两颗星、初版图只印了一颗；图照初版排。
- f21v（1 月 26 日）：正文从“三十角秒”改为照字面的“三十角分”，脚注改为“原文如此（min. 30）。从插图看，这颗星紧挨着木星，应为三十角秒。”

## 各页改动

- **f17v**：拉丁文与初版一致。补了初版误印的注释：`% 1610: apparabant; sollicicus`，`% 1610: exitare tamen caepit`（Favaro 作 haesitare tamen coepi）。
- **f18r**：`eiusmodi` → `eiuscemodi`（初版和 Favaro 都作 eiuscemodi，样张误改了词形）。中文“于是在一月十一日……”是新段落开头，去掉 `\noindent`。
- **f18v**：补注释 `% 1610: proxim`（in eadem proxime recta linea）。图 I.12、I.13、I.15 h.3 复测无误。
- **f19r**：**漏词**：页首缺 `in boream`（初版 18v 末行是 “pau-”，19r 首行是 “lulum in boream attollebatur”），已补上。中文“向北抬起”原已放在 f18v，无须改。
- **f19v**：注释格式整理为 `% 1610: oberat`；缩写统一。
- **f20r**：vicesima；中文删去增译的“起初”（Stella insuper novissime conspecta admodum exigua fuit → “此外，这颗最后看到的星非常小”）。
- **f20v**：vicesimaprima、vicesima；缩写统一。
- **f21r**：vicesima、vicesimaquarta；缩写统一；I.24 h.6 脚注和页尾注释。
- **f21v**：vicesima×3；缩写统一；I.26 h.5 正文与脚注按主编决定改。
- **f22r**：vicesima×2；维基文库错字的注释改为 `% 维基文库录文误作 Stellaeie；1610 作 Stellae`；I.31 h.4 页尾注释。
- **f22v**：II.2 h.7 插图位置（见上）。
- **f23r**：II.6 页尾注释。
- **f23v**：无改动。

## 木星图复测

逐幅用 `jove_measure.py` 复测，并放大扫描核对（I.20 三幅、I.21、I.22 两幅、I.24 两幅、I.30、I.31 两幅、II.6、II.7、II.8 都手工量过）。星数、东西位置、偏离直线的方向与扫描一致，日期和时刻标签无误，不用改。I.24 h.6 放大复核，初版确实只有一颗星（−2.2）。

## 拉丁文与中文的其他核对

- 13 页的起止都与初版断页一致（跨页词 huiuscemodi、configuratio、aberat、minutorum、proxime、media、tantum、secundum、viciniores、occidentalis、medium、orientales 都归在开头所在的页）。
- 数字（时刻、角分、角秒）逐条与初版、Favaro 对过，中文都译对了。时刻、角度的写法全范围统一（序数 hora → “第 N 个小时”，数字 hora → “N 时 M 分”，ab occasu → “日落后”；角度 “N 角分 M 角秒”，零角分省略）。
- 衔接：f17r 末尾（“…talis constitutio:”＋I.7 图）→ f17v “ex parte scilicet…”，中文“……相对位置如下：”→“即东侧有两颗星……”；f23v 末尾 “…stellae duae”／中文整句“二月九日……排列如下：”→ f24r “orientales, et una occidentalis…”，f24r 的中文从图后一句开始。两端都没有重复或遗漏。

## 需要主编决定

1. **`pr. 7`（f20v，I.22）**：初版 “a Iove ad occidentaliorem pr: 7”，承接前面的 “minutorum primorum 5”，是省略句。它不在 DECISIONS 列出的形式里，我没改。可以保留，也可以统一成 `min. 7`（但这样就换了词）。
2. **`trigesima`（f22r）**：DECISIONS 只规定了 vicesima。古典拼法多作 tricesima，要不要一并改？
3. **合写的序数词**（decimatertia、vicesimaprima、vicesimaquarta 等）照 Favaro 合写，同一段里又有分写的（decima octava、vicesima secunda）。要不要统一？
4. **`min. sec.`**：初版 “min. sec. 20”“min. tantum sec. 20” 是 minuta secunda 的写法，我保留了两词（只把 `min. sc.` 改为 `min. sec.`）。如果主编希望角秒一律只写 `sec.`，需要再改 f19r、f19v、f22v 三处。
5. f17v 拉丁文 “Orientalior atque occidentalis reliqua paulo maiores” 去掉了 Favaro 和初版都有的逗号（“occidentalis, reliqua”），f18r “commutationem non in Iove” 也去掉了 Favaro 的逗号。都是样张的处理，我没动。
