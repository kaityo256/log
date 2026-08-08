---
title: "2024年10月15日"
date: 2024-10-15T00:00:00+09:00
lastmod: 2024-10-15T00:00:00+09:00
type: diary
source_month: "d202410.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

プログラミング基礎同演習。人数が少ないなぁ・・・

ストレスチェックした。

PDFの情報を取得するコマンドpdfinfoのインストール。

```sh
brew install poppler
```

```sh
$ pdfinfo hoge.pdf
Title:           
Subject:         
Keywords:        
Author:          
Creator:         LaTeX with hyperref
Producer:        LuaTeX-1.16.0
CreationDate:    Tue Oct 15 18:40:28 2024 JST
ModDate:         Tue Oct 15 18:40:28 2024 JST
(snip)
Pages:           103
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       6094670 bytes
Optimized:       no
PDF version:     1.6
```

最後がまずいんだな。Adobe Acrobatで保存しなおし。

```sh
$ pdfinfo hoge.pdf
(snip)
JavaScript:      no
Pages:           103
Encrypted:       no
Page size:       595.276 x 841.89 pts (A4)
Page rot:        0
File size:       5751853 bytes
Optimized:       yes
PDF version:     1.7
```

これでよし。

えらいせんせいからめーるきた。でんわした。しごとふえた。
