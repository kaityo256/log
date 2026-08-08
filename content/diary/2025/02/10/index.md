---
title: "2025年2月10日"
date: 2025-02-10T00:00:00+09:00
lastmod: 2025-02-10T00:00:00+09:00
type: diary
source_month: "d202502.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

科研費の支払請求書(F-2-1)を提出した。

物理学会の参加申し込みした。

arXivに論文を出す場合、PDFのままだとなぜかコンパイルできず、pdf2psでepsに変換しているのだが、内部にラスタ画像を含む場合、epsファイルのサイズが非常に大きくなる問題があった。これでarXivのファイル制限にひっかかってしまうのでGS側でダウンサンプルした。

```sh
pdf2ps -dPDFSETTINGS=/screen input.pdf output.eps
```

ところがこれをするとデータがおかしくなり、手元ではコンパイルできるが向こうではできない。

```sh
pdftops -level3 -eps -paper match input.pdf output.eps
```

だとファイルサイズが小さくならない。

最終的にどうにもならず、一度PDF→JPG→PDFとしてからEPSに落としてなんとかした。ものすごくアホなことをしている感があるがしょうがない。

arXiv、無事にreplace出した。なんかどうでも良いところで時間かかったなぁ・・・

物理学会の立て替え払い請求書などを整理。
