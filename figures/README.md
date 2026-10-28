# 插图来源

所有扫描图取自 Smithsonian Libraries 藏 1610 年初版（archive.org 条目 `Sidereusnuncius00Gali`，标注 Not in copyright），经 `tools/fetch_scans.py` 去黄。坐标中 `pages` 指 `work/pages/` 的 1/3 尺寸图，`full` 指 `scans/` 的全尺寸图。

| 文件 | 来源 | 做法 |
|---|---|---|
| `luna_1.png` | 扫描 0019（8r） | full 区域 y 2495–4825、x 615–3105；页脚提示词 *Verum* 用左侧 370 px 外的版面纹理覆盖；折痕：`remove_crease.py figures/luna_1.png "0,1165,190,1165,16;170,1190,1880,1148,23;270,1186,540,1186,12"` |
| `luna_2.png` | 扫描 0022（9v） | `crop_ornament.py 0022 372 762 1198 1572`，再去掉顶部 40 px 的正文字脚；折痕：`"0,1276,1200,1283,22,1;1200,1283,1900,1285,20,1;1900,1285,2432,1260,20,1"` |
| `luna_3.png` | 扫描 0023（10r） | 版画顶部压在页眉下：full 区域 x 684–3030、y 560–2664，先擦去页眉铅字（粗笔画连通块）和其下的横向印痕，再按墨迹收紧左右下三边 |
| `luna_4.png` | 扫描 0024 上图（10v） | `crop_ornament.py 0024 392 196 1214 972` |
| `luna_5.png` | 扫描 0024 下图（10v） | `crop_ornament.py 0024 414 988 1214 1704`；折痕：`"1265,659,2125,644,21,1"` |
| `orn_device.png` | 扫描 0005（书名页印刷商标） | `crop_ornament.py 0005 330 1066 1110 1572` |
| `orn_head_a.png` | 扫描 0007（献词页首花饰） | `crop_ornament.py 0007 200 190 1050 370` |
| `orn_head_b.png` | 扫描 0013（5r 页首花饰） | `crop_ornament.py 0013 212 218 1025 390` |
| `orn_initial_P.png` | 扫描 0007（木刻首字母 P） | `crop_ornament.py 0007 190 718 500 1010` |
| `orn_initial_M.png` | 扫描 0013（木刻首字母 M） | `crop_ornament.py 0013 212 878 508 1175` |
| `orn_zh_you.png`、`orn_zh_zai.png`、`orn_zh_da.png` | 新制 | `make_zh_initial.py 有 fonts/NotoSerifSC-Bold.ttf … --seed 3`；`在 … --seed 5`；`大 … --seed 7`（`大` 目前未使用）。宋体粗体、撑满边框，与 1610 年木刻首字母的罗马正体大写对应 |
| `orn_ja_toku.png`、`orn_ja_i.png` | 新制 | 日语版的木刻风格首字「徳」「偉」：`make_zh_initial.py 徳 fonts/NotoSerifJP-Bold.ttf … --seed 3`；`偉 … --seed 5`（`make_fonts.py --ja` 先导出 Noto Serif JP） |
| `chart_*.tex` | 扫描 0038–0040 | `star_chart.py` 生成：`orion`（0038，`90 0 1402 1810 --dropxy "3418,2822;3381,2870" --split "2712,1052;2204,1292"`），`pleiades`（0039，`75 250 1160 915`），`orion_head`（0040，`400 1040 860 1590 --allsmall`），`praesepe`（0040，`895 900 1402 1690`） |

折痕修补的命令都对 `*_orig.png`（第一次运行时自动保存的未修补图）操作，可以调整参数后重跑。`*_orig.png` 不进版本库，可用上表的裁切命令重新生成。

## 封面

`cover_moon.png`、`cover_device.png`：`python tools/make_cover_art.py figures/luna_4.png figures/cover_moon.png`、`… figures/orn_device.png figures/cover_device.png`，把纸色转为透明、墨色转为暖黑，直接印在封面的米色底上。版式见 `front/cover.tex`。
