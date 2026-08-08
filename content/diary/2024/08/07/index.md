---
title: "2024年8月7日"
date: 2024-08-07T00:00:00+09:00
lastmod: 2024-08-07T00:00:00+09:00
type: diary
source_month: "d202408.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

過去の卒論、修論を全てesaにアップロード。

そういえばesaっていつ使い始めたっけ？と調べたら、6/6使用開始＋アカデミックプラン申請、6/11に申請が通り、本格的に使い始めたっぽい。

というわけで過去の日記を追記(禁断の歴史修正)。

こういう情報こそ日記に書くべきだと思うのだが。

esaは10MB以上のファイルを添付できない。いくつかの卒論/修論がこの制約に引っかかってしまったのでlightweight版を作ったが、一つだけどうにもならない。以下は失敗例。

```sh
ps2pdf thesis.pdf output.pdf
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf thesis.pdf
ps2pdf -dPDFSETTINGS=/ebook  thesis.pdf output.pdf  
```

MacのQuartzフィルタの「Reduce File Size」も駄目だった(ファイルサイズが増えた)。

これまでの卒論、修論見てると、そのまま論文になりそうな(でもpublishしていない)結果が結構あって、力不足を感じる。卒論で結果が出た場合は論文まで持っていけているケースが多い(N=3)が、修論で結果が出た場合は学生が卒業してしまうこともあって論文にできていない。頑張らないといけない。

FDアンケートのコメントを返した。
