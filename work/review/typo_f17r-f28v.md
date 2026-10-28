# 字体角色标注：f17r–f28v（扫描 0041–0064）

## 结论

逐页对照 work/pages/NNNN.png 检查了 24 页，有疑问处用 scans/ 全尺寸裁图放大核对（0063 *Sistemate Copernicano*、0064 *Medicea Sidera*、*Planetae MEDICEA*、*Sistemate*）。

- **斜体：0 处。** 这一部分（木星卫星观测日志与结尾）全部用正体排印，正文中没有意大利斜体。木星图里的 Ori./Occ. 和 *fixa*（0060–0062）属于插图，已由 `\jove` 宏自动处理，没有动。
- **大写强调：2 处，都已标注，与初版一致，未作改动：**
  - f17r（0041 第 4 行）**PLANETAS** → `\capsemph{planetas}` / `\zhemph{行星}` ✔
  - f28v（0064 倒数第 7 行）**Planetae MEDICEA** → `planetae \capsemph{medicei}` / `\zhemph{美第奇}行星` ✔（拉丁文词形按 Favaro 作 medicei，行首注释 `% 1610: MEDICEA` 已有）
- 已核对：以下不是大写强调，所以不加宏：0063 *Mediceorum Planetarum*、0064 *Medicea Sidera*（普通首字母大写）；*Sistemate Copernicano*、*Sistemate* 都是正体，不用斜体。
- 没有发现初版里没有强调、本版却加了 `\capsemph` 的地方。
- **本组 24 个文件都没有修改**（文字、断页、木星图坐标、f28v 的 `\taperpar` 结构和 FINIS 一行都保持原样）。

## check_folio

24 页全部 `OK`（各一页）。f28v 报 5 条 `Overfull \hbox (1.01pt)`，位置在 `\taperpar` 段落（第 5 行）。这是原有的情况，我没有改动这一页，与本次标注无关。约 1pt，肉眼看不出，留给主编决定是否处理。

## 各页木刻装饰

| 叶 | 扫描 | 装饰 |
|---|---|---|
| f17r | 0041 | 无 |
| f17v | 0042 | 无 |
| f18r | 0043 | 无 |
| f18v | 0044 | 无 |
| f19r | 0045 | 无 |
| f19v | 0046 | 无 |
| f20r | 0047 | 无 |
| f20v | 0048 | 无 |
| f21r | 0049 | 无 |
| f21v | 0050 | 无 |
| f22r | 0051 | 无 |
| f22v | 0052 | 无 |
| f23r | 0053 | 无 |
| f23v | 0054 | 无 |
| f24r | 0055 | 无 |
| f24v | 0056 | 无 |
| f25r | 0057 | 无 |
| f25v | 0058 | 无 |
| f26r | 0059 | 无 |
| f26v | 0060 | 无 |
| f27r | 0061 | 无 |
| f27v | 0062 | 无 |
| f28r | 0063 | 无 |
| f28v | 0064 | 无木刻。结尾段落排成倒三角，下面是字距拉开的 F I N I S，没有尾花或花饰 |

## 疑问

无。
