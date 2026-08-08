---
title: "2022年12月16日"
date: 2022-12-16T00:00:00+09:00
lastmod: 2022-12-16T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

スマホのアラームで目を覚まし、Todoistの「おはようございます。今日は9つのタスクが予定されています」の表示をみてげんなりする。

午前中は打ち合わせ。

細かいTODOを潰していく。サーバ室のハブにテプラ貼ったりとか。

プログラミング基礎同演習のスライド、一部表示がおかしくなっていたのを修正。ついでにSpeaker Deckの[コレクション](https://speakerdeck.com/kaityo256/collections/python)にまとめた。

打ち合わせ。

久しぶりにRe:VIEWで製本する環境を構築。まずredcarpetがないな。Gemfileにredcarpetを追加。

```rb
source 'https://rubygems.org'

gem 'redcarpet'
gem 'rake'
gem 'review', '2.5.0'
```

```sh
bundle config path vendor/bundle
bundle install
```

これでいけるはず？

だめだ。redcarpetはrequireできるが、redcarpet/render/reviewがrequireできない。

諦めて`sudo gem`でやる。

```sh
sudo gem install redcarpet
```

まだうまくいかない。redcarpetのRe:VIEW対応が消えてて、HTMLとXHTMLしかなくなってるっぽい。

md2review でなんとかする。

```sh
sudo gem install md2review
```

後は[一週間でなれる！スパコンプログラマ](https://github.com/kaityo256/sevendayshpc)のファイルをコピペしてなんとかした。

そうだ、思い出した。「一週間でなれる！スパコンプログラマ」はmd2reviewで行けたんだけど、「ゼロから学ぶPython」で同じことをしようとしたら数式がうまく変換できず、それでredcarpetでなんとかしたんだった。

[筑波大学学園祭 Web サイト構築の舞台裏](https://zenn.dev/inaniwaudon/articles/e4d6d326c4c18b)

「なにこれ？技術力たっか！」と思ったが、著者を見て納得した。

[筑波大の授業DBを自作して大学公認にした人](https://www.itmedia.co.jp/news/articles/2104/30/news147.html)ですね。っていうか学部2年生でしたか。なんかもっと昔から活躍していたような。

これだ。

[強力なグラフィック機能を備えた組版処理システムTwight](https://note.com/ipsj/n/n6f6961254850)

当時高校生だったのか……
