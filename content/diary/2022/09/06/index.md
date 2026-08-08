---
title: "2022年9月6日"
date: 2022-09-06T00:00:00+09:00
lastmod: 2022-09-06T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

修理に出してたMacBookPro返ってきた。SSDの不具合。ボード一体型なので、ロジックボード全交換。それじゃ再インストールできないのも無理はないし、素人にはどうしようもない。すぐにプロに任せればよかった。

Subversionのリポジトリの状態をプロンプトに出す奴、これまで`LANG=C`を指定していたが、日本語(UTF-8)のファイルを管理するようになってバグるのでやめた。また、昔はdepthとしてimmediateを指定していたが、これももう速度が許容範囲になったので、その指定も外した。

っていうかもうSubversion管理やめるかなぁ。少なくとも予算管理はsvn+xlsxよりGoogle SpreadSheetの方が便利な気がする。ただ、Google Oneの入会必須。Paper PileもGoogle Drive使うから、こちらもGoogle One要求。もう入るのは確定。あとは支払い方法を検討するだけだな。

学習指導のお仕事。

dvipdfmxがPDFのバージョンが古いとワーニングを出す。`-V`でマイナーバージョンを指定。とりあえず`-V 7`でいいのかな。`.latexmkrc`はこうなる.

```perl
#!/usr/bin/env perl

$latex = 'platex -synctex=1 %O %S';
$bibtex = 'pbibtex %O %B';
$makeindex = 'memindex %O -o %D %S';
$pdf_mode = 3;
$dvipdf = 'dvipdfmx -V 7 %O -o %D %S';
```

Macでどうなるか確認しないと。
