# 星际信使 · Sidereus Nuncius（1610）拉丁文—中文对照本

伽利略《星际信使》（威尼斯，1610）的重排对照本：左栏现代拼写的拉丁文，右栏直接译自拉丁文的中文。用 XeLaTeX 排版，**每页对应初版的一页**，页眉、断页、字体分工照初版，木星卫星图、星图、几何示意图按初版逐点测量重绘为矢量图，月面铜版画和木刻装饰取自初版扫描并经去黄、折痕修补。

成书 PDF 见 [Releases](../../releases)。

<p align="center">
  <img src="showcase/00_cover_front.jpg" width="24%">
  <img src="showcase/02_献词_2r.jpg" width="24%">
  <img src="showcase/04_月面铜版画_10v.jpg" width="24%">
  <img src="showcase/05_星图_16bv.jpg" width="24%">
</p>

## 构建

需要 TeX Live（XeLaTeX、ctex、paracol、lettrine、tikz）和 Python 3（Pillow、numpy、scipy、PyMuPDF、fontTools）。

```bash
python tools/make_fonts.py        # 从 Noto Serif SC 可变字体导出三档静态字重到 fonts/
python tools/build_book.py        # 由 text/ 生成 folia/，编译两遍并检查左右页与溢出 -> main.pdf
```

文字的唯一来源是 `text/`：改拉丁文改 `text/la.yaml`，改中文改 `text/zh.yaml`，改版面（插图位置、特殊排版块）改 `text/layout.yaml`。`folia/` 下的页面文件由 `tools/gen_folia.py` 生成，不要手改。

楷体（献词、斜体对应）用的是 Windows 自带的 KaiTi；在其他系统上请在 `preamble.tex` 里把 `zhkai` 换成本机的楷体字体。

只改某一页时：先 `python tools/gen_folia.py`，再 `python tools/check_folio.py f17v`，检查这一页是否正好排满一页并生成预览图。

### 英语版（Latin–English）

`python tools/build_book.py --lang en` → `main_en.pdf`。英语译文在 `text/en/part1–5.yaml`（按句，键为 `p012.03`），规范与术语表见 `work/EN_TRANSLATION.md`。英语和拉丁文语序接近，所以英语也按原文断页：跨页的句子在英译中对应位置插入同样的断页标记（如 `⟦8v⟧`），生成时在那里切开；`tools/list_breaks.py en` 列出全部 48 个跨页句子及其标记情况。少数排得满的页由 `tools/fit_pages.py --lang en` 微调该页的字号行距（记录在 `text/layout.yaml` 的 `tr_size`/`la_size`）。

### 增加其他语言的译文

按句翻译即可，不必考虑分页：在 `text/<语言>.yaml` 里为 `la.yaml` 的每一句写一条译文，键为“段落.句号”（如 `p012.03`）。`python tools/gen_folia.py --lang en` 会把每句译文放进其拉丁原句开头所在的对齐块，也就是所在的那一页。`tools/test_distribution.py` 检查这一分配：每句恰好出现一次、位置正确。

## 目录

| 路径 | 内容 |
|---|---|
| `main.tex`、`preamble.tex` | 总控文件与导言区（版式、字体分工、木星图与星图宏、倒三角收尾） |
| `front/` | 本版书名页与编辑说明 |
| `text/la.yaml` | 拉丁文：按段落、按句编号，一句一个键；`⟦8v⟧` 标出初版断页，`⟦\|⟧` 标出同一页内的对齐块分界（多在插图处） |
| `text/zh.yaml` | 中文：按对齐块存放，与拉丁文的块一一对应 |
| `text/layout.yaml` | 每一叶的结构：页面样式、对齐块、插图和特殊排版块的顺序 |
| `folia/fNNx.tex` | 生成的页面文件，每个文件是初版的一页（如 `f08v` = 第 8 叶背面），不进版本库 |
| `figures/` | 插图；来源与生成命令见 `figures/README.md` |
| `tools/` | 去黄、测量木星图、星图提取、折痕修补、木刻首字生成、拼写统一、编译检查等脚本 |
| `work/` | 编辑规范 `CONVENTIONS.md`、编辑决定 `DECISIONS.md`、叶码对照表、拉丁文底本、各阶段的工作与校对记录 |

扫描图不在仓库里，需要时运行 `python tools/fetch_scans.py` 下载并去黄（约 400 MB）。

## 来源

- **拉丁文**：A. Favaro 编《伽利略全集》国家版第三卷（1892），录自拉丁文维基文库；与 1610 年初版逐页核对，按现代拼写转写。
- **扫描**：Smithsonian Libraries 藏 1610 年威尼斯初版，Internet Archive 条目 [`Sidereusnuncius00Gali`](https://archive.org/details/Sidereusnuncius00Gali)（Not in copyright）。
- **字体**：EB Garamond、Noto Serif SC（均为 SIL Open Font License）。

## 署名

编译：[metachow](https://github.com/metachow)
协作：Claude（Anthropic），参与翻译、校对、排版与插图处理。

中文译文由 AI 协作完成，尚未经拉丁文专家审校；发现错误欢迎提 issue 或 PR。

## 许可

| 内容 | 许可 |
|---|---|
| 中文译文、注释、编辑说明、LaTeX 排版源码（`main.tex`、`preamble.tex`、`front/`、`folia/`、`work/` 中的文档）、重绘的矢量插图 | [CC BY 4.0](LICENSE)，使用时请署名 metachow 并注明出处 |
| `tools/` 中的脚本 | [MIT](tools/LICENSE) |
| 拉丁原文、1610 年初版扫描及取自扫描的铜版画与木刻 | 公有领域 |
| EB Garamond、Noto Serif SC 字体 | SIL Open Font License（字体文件不随仓库分发） |
