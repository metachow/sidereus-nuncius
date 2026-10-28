# 《星际信使》拉丁文—中文对照本：工作规范

> **2026-10-28 起的变化**：文字的唯一来源改为 `text/`（`la.yaml`、`zh.yaml`、`layout.yaml`），`folia/*.tex` 由 `tools/gen_folia.py` 生成，不再手改。下文第 1 节描述的是生成出来的页面文件格式，仍然有效；修改时请改 `text/` 里对应的条目，然后重新生成。翻译新语言时按句写 `text/<语言>.yaml`，见 README。

所有参与转写、翻译、校对的人（包括 subagent）都按本文件执行。有疑问时以本文件和已完成的样张（`folia/f06v.tex`–`f08r.tex`、`f17r.tex`–`f18r.tex`）为准。

## 0. 项目结构

| 路径 | 内容 |
|---|---|
| `preamble.tex` | 公用导言区与宏，**不要修改** |
| `main.tex` | 总控文件，**不要修改** |
| `folia/fNNx.tex` | 每个文件对应 1610 年初版的一页（如 `f08v.tex` = 第 8 叶背面） |
| `folia/order.tex` | 阅读顺序，由主编维护，**不要修改** |
| `work/folio_map.tsv` | 扫描页号 ↔ 初版叶码 ↔ 文件名 |
| `work/pages/NNNN.png` | 去黄后的扫描页，1/3 尺寸（约 1400×1940），供阅读 |
| `scans/NNNN.png` | 同上，全尺寸（约 657 dpi，4200×5800），供测量木星图 |
| `work/latin_favaro_wikisource.txt` | 拉丁文底本：Favaro 编国家版（1892），录自拉丁文维基文库 |
| `tools/check_folio.py` | 单页编译检查：`python tools/check_folio.py f08v` |
| `tools/jove_measure.py` | 测量木星图：`python tools/jove_measure.py scans/0045.png` |

叶码：扫描第 5 页 = 第 1 叶正面（书名页）。正面（r）页眉为 RECENS HABITAE 并带叶码，背面（v）页眉为 OBSERVAT. SIDEREAE。第 16、17 叶之间有两张无叶码的星图叶，记作 16a、16b。

## 1. 每页文件的格式

```latex
\folium{8v}

\LA
\noindent Verum non modo ...        % 拉丁文段落（左栏）

\ZH
\noindent 然而，不仅……              % 对应的中文段落（右栏）

\spanfig{\jove[I.\,13]{-2.1/1, 3.0/1}}   % 跨两栏的插图，放在两种文字的相同位置

\LA
Sequens paragraphus ...

\ZH
下一段……

\folioend
```

- `\LA` 开始一段拉丁文，并与上一对段落顶端对齐；紧接着用 `\ZH` 写它的中文。**每一对段落都是 `\LA` 然后 `\ZH`**。
- 同一语言连续两段，第二段之前不要再写 `\LA`／`\ZH`，空一行即可（参见 `f07r.tex`）。
- 页面开头如果是上一页延续下来的半句或半段，段首加 `\noindent`。
- 每个文件**必须正好排成一页**。写完后运行 `python tools/check_folio.py fNNx`，结果必须是 `OK`，并打开它生成的 PNG 看一眼版面。若溢出，先检查是否把下一页的文字也放了进来；确实是因为插图太多排不下，就在文件末尾用注释 `% OVERFLOW: ...` 说明，交给主编处理，**不要修改 preamble.tex 的字号或行距**。
- 意大利文页面（出版许可）：在 `\LA` 之后加 `\selectlanguage{italian}`。
- 初版**没有页眉**的页（书名页、献词、出版许可、f05r、只有插图的整页）用 `\folium*{2r}`：不印页眉，只印叶码。初版的空白页用 `\blankfolium{1v}`（已建好 `f01v.tex`）。

**另见 `work/DECISIONS.md`**：主编对各组提出问题的决定。它的效力优先于本文件，校对时必须逐条执行。

## 2. 断页规则（保持初版分页）

1. 拉丁文**严格按初版断页**，每个文件只放初版这一页上的文字。
2. 跨页断开的单词（如 `Per-|spicillis`），整个词放在它**开头所在**的那一页。
3. 页脚的提示词（catchword，下一页第一个词的预印）、帖号（如 `E`、`E 2`）、页眉、叶码都**不录入**。
4. 中文尽量在**与拉丁文断页相应的分句处**断开；中文语序无法拆分时，**整句放在它开头所在的那一页**。因此一页的中文可能比拉丁文多出或少掉半句，这是允许的。
5. 插图放在初版中它所在的位置。若初版插图夹在句子中间，统一放在**引出它的那个分句之后**（如 “…talis constitutio:” / “……排列如下：” 之后），这也是 Favaro 本的做法，两栏同步。只有放不下、会跨页的图才放在本页末尾，并在行末加注释说明。

## 3. 拉丁文转写（现代拼写）

以 Favaro 本为底本，**逐句与初版扫描核对**：初版有而 Favaro 本缺的、两者词序不同的，以初版为准；Favaro 对初版明显印错之处的校正，采用 Favaro 的读法，并在该行末加 LaTeX 注释 `% 1610: <初版原文>`。

拼写规则：
- `æ`、`œ` 拆写为 `ae`、`oe`；长 s（ſ）作 s；u/v 按音值区分；i 保持（`Iuppiter`、`Ianuarii`、`eius`），不用 j。
- 缩写一律展开（`q;` → `que`，`ā`/`ē` 等鼻音符号 → `am/an/em/en`，`&` → `et`）。
- 只改拼写，不改词汇：Galileo 自造或晚期拉丁语的词形保持原样（如 `quatercentuplam`、`bisdecuplo`）。统一为古典拼法的例子：`quatuor → quattuor`，`nunquam → numquam`，`intelligo → intellego`，`expecto → exspecto`，`caeteri → ceteri`，`plerunque → plerumque`，`circundo → circumdo`，`extat → exstat`，`literae → litterae`，`reperi`（完成时）`→ repperi`，`quinimmo → quin immo`，`adinvicem → ad invicem`。
- 大小写：普通名词小写（`perspicillum`、`stella`、`planeta`、`instrumentum`）；天体名称保留大写（`Sol`、`Luna`、`Tellus`、`Terra`、`Iuppiter`、`Venus`、`Mercurius`、`Saturnus`、`Galaxia`）；人名、地名大写。句首大写。
- 初版用**全大写字母强调**的词（如 `PLANETAS`、`NEBULOSAS`、`MEDICEA SIDERA`），排作小型大写：`\textsc{planetas}`；中文对应词用 `\zhemph{行星}`。
- 标点按 Favaro 本，必要时参照初版。

## 4. 中文翻译

- **直接从拉丁文翻译**。可以参考公有领域的 E. S. Carlos 1880 年英译本帮助理解，但**不得抄录或贴近改写任何现代出版的译本**（包括 Van Helden 1989 年英译本和已出版的中译本）。译文必须是新的。
- 文体：准确、通顺的现代汉语书面语，不用文言。拉丁文长句可以拆成几个中文句子，但不得增删信息。人称照原文（伽利略在“我”和“我们”之间切换，照译）。
- 日期写作“一六一〇年一月七日”“一月十二日”，正文中的数字一般用汉字；角度、时刻照下面术语表。
- 标点用全角中文标点，引号用“”，书名号《》。拉丁字母（图中字母 A、B、C 等）前后各空半格，照样张。
- 原书括号内的话照样放在括号里。

### 术语表（必须统一）

| 拉丁文 | 中文 | 说明 |
|---|---|---|
| perspicillum | 望远镜 | 伽利略尚未使用 telescopium 一词；统一译“望远镜” |
| specillum；perspicilla（复数，指镜片） | 镜片 | 依上下文 |
| organum, instrumentum | 仪器 | |
| stellae fixae, inerrantes | 恒星 | |
| stellae vagae, erraticae, planetae；vaga sidera | 行星；游星 | `vaga sidera` 译“游星” |
| Medicea Sidera | 美第奇星 | |
| Iuppiter | 木星 | |
| Luna | 月球（天体）／月亮（描述所见景象时可用） | |
| Tellus, Terra | 地球 | |
| Galaxia, Lacteus Circulus | 银河 | |
| stellae nebulosae | 星云状星 | 首次出现可加注 |
| Nebulosa Orionis | 猎户座星云 | |
| Praesepe | 鬼星团（蜂巢星团） | 首次出现写“鬼星团（蜂巢星团）” |
| Pleiades | 昴星团 | |
| Cingulum et Ensis Orionis | 猎户座腰带与佩剑 | |
| magnitudo（星的） | 星等；大小 | 明确指分等时用“星等” |
| maculae magnae, antiquae | 大斑，古斑 | 加引号首次出现 |
| terminus (lucis et tenebrarum) | 明暗交界线 | |
| coniunctio（月） | 合朔 | |
| ecliptica | 黄道 | |
| zodiacus | 黄道带 | `iuxta longitudinem zodiaci` 译“沿黄道经度方向” |
| minutum (primum), scrupulum primum | 角分 | |
| secundum, scrupulum secundum | 角秒 | |
| hora noctis prima / secunda | 入夜后第一个／第二个小时 | 意大利计时法从日落起算；说明意大利计时法的脚注由主编加在 f17r（首次出现处），其他页不要重复 |
| orientalis / occidentalis | 东侧（的）／西侧（的） | 图中 Ori. / Occ. 不译 |
| Cosmus Medices II | 科西莫·德·美第奇二世 | |
| Magnus Etruriae Dux | 托斯卡纳大公 | |
| Florentia, Venetiae, Patavium | 佛罗伦萨，威尼斯，帕多瓦 | |
| Belga | 一个尼德兰人 | |
| philosophi | 哲学家 | |

遇到术语表没有的重要术语或人名，自行决定译法并**记入你的工作记录**（见第 7 节），不要修改本文件。

### 脚注

- 只在读者需要时加：度量单位、天文背景、历史人物、伽利略与现代认识明显不同之处、Favaro 本与初版的重要异文。一般每页 0–2 条，力求简短。
- 脚注写在中文栏里，用 `\footnote{...}`，内容为中文。

## 5. 插图

| 类型 | 做法 |
|---|---|
| 木星卫星图（`Ori. * ○ * Occ.`） | `\spanfig{\jove[日期]{在线上的星}[偏离直线的星]}`。坐标用 `python tools/jove_measure.py scans/NNNN.png` 测量（自动找出该页所有木星图）；自动没找到的，用 `--y <纵坐标> --x <横坐标>`（全尺寸像素，约等于 `work/pages` 图上坐标 ×3）。**务必对照扫描核对**：去掉误检的污点，补上漏检的星（距直线超过约 0.9 个木星直径的星检测不到，需手工估计）。尺寸取 1、1.3 这类简单值即可，伽利略文字里说“较大”的星给 1.3 左右。日期标签写作 `I.\,13`（罗马数字月份 + 日），同一夜多幅图时加时刻，如 `I.\,15, h.\,3`。图旁另有文字（如时刻说明）的，放进日期标签或正文，不要漏掉。图中的**恒星**放进第四个可选参数，会在星旁自动标 *fixa*：`\jove[II.\,26, h.\,5]{-2.0/1, 3.1/1}[][4.0/1/-1.2]`（没有离线行星时第三个参数留空 `[]`）。 |
| 月面图、星图、几何示意图、书名页印刷商标、装饰图案 | 先放占位符：`\spanfig{\placeholderfig[高度]{扫描 0024：两幅月面图（上弦、下弦）}}`，高度大致按初版中插图占页面的比例估计（版心高约 210 mm）。之后由主编裁图或重绘。 |

## 5a. 字体分工（照初版）

| 初版 | 拉丁文 | 中文 |
|---|---|---|
| 罗马体正文 | 默认 | 默认（思源宋体，`fonts/` 中的静态字重） |
| 意大利斜体 | `\lital{..}`；整段斜体（献词）用 `\LAi` | `\zhital{..}`（楷体）；整段用 `\ZHi` |
| 斜体说明句中的花式大写 | `\litsw{..}`，只用于大小写混排的行 | — |
| 正文大写强调 | `\capsemph{..}`（括号内照常小写） | `\zhemph{..}`（粗体） |
| 大写标题 | `\dispcaps[字号][字距]{..}` | `\zhdisp[字号]{..}`（半粗） |
| 木刻首字母、页首花饰 | `\woodinitial{P}{raeclarum}`、`\headpiece{a}`（图在 `figures/orn_*.png`，用 `tools/crop_ornament.py` 裁） | — |

初版中斜体只出现在书名页、献词和 5r 的副标题；正文（5v–28v）全是正体。书名的斜体（如 *De systemate mundi*）是编辑加的现代惯例，用 `\textit`，与初版斜体无关。

## 6. 不要做的事

- 不改 `preamble.tex`、`main.tex`、`folia/order.tex`、本文件，也不改别人负责的叶。
- 不要编译整本 `main.tex`（多个 agent 同时写 `main.pdf` 会冲突），只用 `tools/check_folio.py`。
- 不自行重画月面图或星图。
- 不在 `scans/`、`work/pages/` 里写文件。

## 7. 工作记录

每个 agent 在 `work/notes/<任务名>.md` 写一份简短记录：
- 完成了哪些叶，`check_folio` 结果；
- 新增术语的译法；
- 拉丁文与初版／Favaro 的异文及处理；
- 拿不准、需要主编决定的地方（具体到叶码和句子）。
