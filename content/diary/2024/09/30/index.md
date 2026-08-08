---
title: "2024年9月30日"
date: 2024-09-30T00:00:00+09:00
lastmod: 2024-09-30T00:00:00+09:00
type: diary
source_month: "d202409.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

VSCodeでLaTeXを保存すると「LaTeX formatter is set to "none" by formatting.latex.」というエラーが出る。これはLatex-workshopの設定でフォーマッタがNoneになっていることを示す。

設定のLatex-workshop＞Formatting＞Latexのプルダウンメニューから「latexindent」を選ぶか、`setting.json`に

```json
"latex-workshop.formatting.latex": "latexindent"
```

と記入すればOK。
