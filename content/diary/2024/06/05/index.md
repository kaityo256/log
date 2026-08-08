---
title: "2024年6月5日"
date: 2024-06-05T00:00:00+09:00
lastmod: 2024-06-05T00:00:00+09:00
type: diary
source_month: "d202406.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

```sh
$ dmd pptxgrep.d
pptxgrep.d(8): Error: unable to read module `xml`
pptxgrep.d(8):        Expected 'std/xml.d' or 'std/xml/package.d' in one of the following import paths:
import path[0] = /usr/local/opt/dmd/include/dlang/dmd
```

xmlライブラリが読み込めない。

五億年ぶりにMacでD言語のコードをコンパイル。

```sh
brew upgrade dmd
dub fetch dxml
```

でもコンパイルできない。いろいろ調べたが、[`std.xml`がobsoleteになっているらしい？](https://docarchives.dlang.io/v2.094.0/phobos/std_xml.html)

```txt
Warning: This module is considered out-dated and not up to Phobos' current standards. It will be removed from Phobos in 2.101.0. If you still need it, go to https://github.com/DigitalMars/undeaD
```

```txt
$ dmd --version
DMD64 D Compiler v2.109.0

Copyright (C) 1999-2024 by The D Language Foundation, All Rights Reserved written by Walter Bright
```

Phobosのバージョンとコンパイラのバージョン一致しているの？なら2.109だから、std.xmlは消えたんだな。

ってことは今はpptxgrepは再コンパイルしたら使えないのか。また別の言語で作り直すかなぁ。次は何でやるかなぁ。

[Lion CoveとSkymontの詳細が明らかに。Hyper-Threading「非対応」で電力効率爆上げ](https://pc.watch.impress.co.jp/docs/news/event/1596852.html)

ついにHT廃止ですか。

なんとなく昔のスライドをサルベージした。

[ハイパースレッディングの 並列化効率への影響](https://speakerdeck.com/kaityo256/hyper-threading)
