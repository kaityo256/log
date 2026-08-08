---
title: "2021年2月24日"
date: 2021-02-24T00:00:00+09:00
lastmod: 2021-02-24T00:00:00+09:00
type: diary
source_month: "d202102.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

GitHub Typoという、GitHubにあるリポジトリのありがちなタイポを見つけてリンクするという、とてもおせっかいなサイトに捕捉されたので修正する。ispellとaspell試したけど、aspellの方が使いやすいな。ただ、オプションが面倒。こんな感じかな。

```sh
aspell --lang=en -x -c -t fiename
```

* `--lang=en` 英語にする
* `-t` モードをTexモードにする
* `-x` = `--dont-backup` バックアップしない
* `-c` Spell check a single file.

一気に調べるには

```sh
aspell --lang=en -t list < ワイルドカード | sort -u |less
```

が便利。例えば`**/*.md`で調べるなら、

```sh
aspell --lang=en -t list < **/*.md | sort -u |less
```

これで出てきた一覧のうち、明らかにTypoなのをgrepで場所を特定して修正するのが便利。

データベースを作って、論文として出版するという方法。

Scientific data (Nature) IF 5.541

「TACMIコンソーシアム」[http://www.utripl.u-tokyo.ac.jp/tacmi/](http://www.utripl.u-tokyo.ac.jp/tacmi/)
一言でいうとNDAで守られた学会。通常の学会で発表すると「公知の事実」になってしまうので、企業の人が発表しやすいように作られたとのこと。
