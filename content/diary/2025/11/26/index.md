---
title: "2025年11月26日"
date: 2025-11-26T00:00:00+09:00
lastmod: 2025-11-26T00:00:00+09:00
type: diary
source_month: "d202511.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Tahoeになってから、「ブラウザからターミナルにフォーカスを移そうとしたら、しばらく反応しない」というのが頻発。
頻発といっても一日に数回なので、現場を抑えることが難しい。調べたら[オートフィルヒューリスティックが悪さをしている](https://iboysoft.com/howto/macos-tahoe-freezing.html)っぽいのだが、その現場を押さえられない。オートフィルのCPU利用率を監視するため、

```sh
top -o cpu -stats pid,command,cpu,mem,time | grep -i autofill
```

を実行して、しばらくブラウザで作業して、戻ったのだが何もおきない。うーむむ。

なんか、Windowsで作業してからMacを開くと起きるっぽい。しばらく放置してから触るのがトリガーっぽいな。

論文一つ修正完了。土曜日には再投稿したい。

物性研スパコンの申請、仮申請して、申請書をあらかた書いた。
