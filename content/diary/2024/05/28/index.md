---
title: "2024年5月28日"
date: 2024-05-28T00:00:00+09:00
lastmod: 2024-05-28T00:00:00+09:00
type: diary
source_month: "d202405.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理のK-LMSのモジュール公開した。完全に自転車操業。

明日、新計算原理の報告会だ。

Webサーバのmariadbの生存確認スクリプト、crontabで実行したスクリプトが標準出力、標準エラー出力になにか吐いたらメールが飛ぶの知らずに、死ぬほどメールが飛ぶ仕様になってた。しかも毎分確認してたので、メールがrootに12000通とか来てた。とりあえずメールを飛ばさないように修正。

cronで実行しているcertbotもメールを飛ばすが、こちらは一日一回だからいいかな。

JFMのstyleを試そうとしたが、どうもローカルのtexliveが古い？

とりあえず最新にしてみる。

```sh
curl -OL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar xvf install-tl-unx.tar.gz
cd install-tl-2*
sudo ./install-tl
```

2時間かかると出てきたな・・・。
