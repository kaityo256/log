---
title: "2019年2月7日"
date: 2019-02-07T00:00:00+09:00
lastmod: 2019-02-07T00:00:00+09:00
type: diary
source_month: "d201902.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

打ち合わせ。

昨日のゼミで面白かった、「ロジスティック回帰でイジング模型の相を判定する」奴、[Qiitaに記事化](https://qiita.com/kaityo256/items/0334b98b8595dbccbad4)しておいた。

git submoduleの使い方に慣れてきた。特にsubmoduleが更新されたら、メインプロジェクトが修正された、ということになるのが理解できなかった。
「submoduleの指すコミット先」という状態が変化する、というイメージかな。これまで、ライブラリとプロジェクトを独立に管理してて、
単に外部ディレクトリで指定してるだけだったから、いつかメインプロジェクトとsubmoduleの連携がおかしくなったときに「動いていた時はどのハッシュだったか」がわからなくなるのはまずいわけか。

少しずつ頭がまわりつつあるが、まだ本調子じゃないなぁ。

5秒早くなっただけか・・・。

数独の高速化で必要だったので[ストップウォッチライブラリ](https://github.com/kaityo256/stopwatch)作った。
内部で__rdtscpを呼んでいるのだが、その調べ物で[こんな技術ブログ](http://proc-cpuinfo.fixstars.com/2014/11/rdtscp-html/)見つけた。フィックスターズという会社のブログで、もともと技術者集団として名高いが、しっかしガチなエンジニアかかえてるな、と思って著者を見てみたらtanakmuraさんだった。まぁ、そうだよな。

タイヤ交換した。これでスタッドレスはラストシーズンかな。
タイヤ交換中暇だったのでQiitaに[Windows Bitmap Fileライブラリ](https://qiita.com/kaityo256/items/777b04fe09980591a28f)の記事かいた。最近Qiitaにたくさん記事書いているけど、まぁ
ウェブサイト移行とリポジトリの掃除の副産物ですね。

数独高速化。現在。

```sh
# before
./a.out difficult.txt > test.dat  81.61s user 0.98s system 99% cpu 1:23.18 total
# after
./a.out difficult.txt > test.dat  76.52s user 1.15s system 98% cpu 1:19.23 total
```

理論系送別会。花束とかいただいた。ありがたいことです。
また、いろいろご心配をおかけしました。
