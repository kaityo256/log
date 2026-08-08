---
title: "2018年11月7日"
date: 2018-11-07T00:00:00+09:00
lastmod: 2018-11-07T00:00:00+09:00
type: diary
source_month: "d201811.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

メーリングリストマネージャ(MLM)の現在。

* <a href="http://old.greatcircle.com/majordomo/">Majordomo</a> 昔よくこれが使われていたが、現在は更新されていない。最終更新 2000年。
* <a href="http://www.fml.org/">fml</a> 国産のメーリングリストマネージャ。インターネット黎明期(1990年代の後半から2000年前半にかけて?)によく使われていたMLM。「fml 設定」とかで検索をかけると2000年代の記事がよくひっかかる。
今回調べてみたらまだ更新されており、非常に驚いた。
* <a href="http://www.list.org/">GNU Mailman</a>これも昔からよく使われているMLM。
* <a href="http://www.lsoft.com/products/listserv.asp">LISTSERV</a>。世界初のMLMらしい。詳しくは知らない。

　他にもSympaとかDada Mailなどがあるらしいが、詳しくは知らない。

　もともと、Mailmanの設定画面があまりに古臭いので、もうMailmanのメンテは死んだのかと思っていたら我々が使っているのがMailman2で、
いまはMailman3が出ていることを知ったのがはじまり。あと、Mailman3はDockerで起動することが推奨というか想定されているらしい。

　なんというか、インターネット黎明期を知るものとして、最近の技術革新には目を見張るというか、もはや完全に置いていかれている状況だ・・・。

```sh
$  git clone -b unstable --depth 1 https://github.com/lammps/lammps.git mylammps
$ cd mylammps
$ mkdir build 
$ module load cmake 
$ cmake ../cmake  
$ make
```

　とりあえずこれでいける。ccmakeでコンパイラを変えたらビルドもできた。


　歯医者。二本目終了。次が最後かな。

　CMP-MLからTwitterへの転送、うまくいった。
いろいろ面倒だったな・・・。

　まとめると、

* WordPressを自前で運用
* メーリングリスト用にMailmanを運用
* メール投稿をするためにPostieプラグインを利用
* 投稿された情報をTwitterに転送するためにNextScripts: Social Networks Auto-Poster (SNAP)を利用


　という感じですか。SNAPからTwitterにアクセスするためにはTwitter Appsの設定が必要で、それが面倒くさかった。
