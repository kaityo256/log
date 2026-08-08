---
title: "2022年10月24日"
date: 2022-10-24T00:00:00+09:00
lastmod: 2022-10-24T00:00:00+09:00
type: diary
source_month: "d202210.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

免許更新。優良者講習会。前から思ってたんだけど、二輪と四輪が同じ道路を走るって、わりと無理がある気がする。

とあるサイトにアクセスしようとしたら503。しかし、「Error 503 first byte timeout」ってメッセージ、初めてみたな。

物理情報工学ソフトウェア開発演習、座学4回のレポート回答の返事をアップロードした。

研究室訪問の準備した。

論文修正。なぜかMacではコンパイルできない。graphicxでdvipdfmxオプションの指定が必要っぽいのだが、WSL(Ubuntu)では問題なくコンパイルできている。PTEPのスタイルでgraphicxをusepackageしているため、追加でオプションをつけてusepackageしてしまうとOption clashで落ちてしまう。うーむ。

時間がないのでWSLで作業する。あー、なんかpush忘れしている。また、学校のマシンにBLASやLAPACKが入ってない。入れる。

```sh
sudo apt-get install libblas-dev liblapack-dev
```
