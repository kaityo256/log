---
title: "2024年4月2日"
date: 2024-04-02T00:00:00+09:00
lastmod: 2024-04-02T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

疲れが残っている。

僕の学位取得年月日は2004年3月25日。なんか必要だったので学位記を引っ張り出した。この情報、10年に一度くらい必要になるんだけど、researchmapとかORC-IDとかで公開できないもんかな。

久しぶりにresearchmapにログインしたら、英語所属が名古屋大学になってた。久しぶりすぎた。

指導委託の書類送付。

研究室所属学生＋利用室提出。

昨日の疲れが残っている中作業しているのでミスが目立つし、そもそも効率が非常に悪い。

ImageMagickのコマンド群の一つ`identify`を初めて知った。こんな感じに使う。

```sh
$ identify test.jpg 
test.jpg JPEG 3840x2160 3840x2160+0+0 8-bit sRGB 388362B 0.000u 0:00.002
```

format文字列が指定できる。いろいろ自動処理に使えそう。Awkと組み合わせるとか。

```sh
$ identify -format "%w %h\n" test.jpg
3840 2160
```

気になってちゃんと調べたら、ImageMagickのコマンドはconvert, mogrity, indentify, montage, composite, displayの6つらしい。思ったより少なかった。

今調べたら、全部`magick`というコマンドから呼び出せる形になってる。magickは2016年にリリースされたバージョン7から導入され、`convert`は後方互換性のために残されてるとか、そういう位置づけっぽい。知らなかった。

8年も前の変更を知らずに生きていたのか。どんどん世界に取り残されているなぁ・・・

物性研スパコンのジョブ投入権更新＋新規追加。

輪講の準備。一節できなかった。明日か明後日できるか？
