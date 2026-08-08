---
title: "2023年4月8日"
date: 2023-04-08T00:00:00+09:00
lastmod: 2023-04-08T00:00:00+09:00
type: diary
source_month: "d202304.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Twitter、API有料化によりtwilogやTwitter検索が死んだ。サードパーティアプリを大事にしないと普通にサービス死ぬと思うけどなぁ。

WSLにおいたPDFにコメントを入れていくとたまに表示がおかしくなる。おそらく中間ファイルの問題。PDFをWindowsファイルシステム側においたら問題が起きなくなった。たまにWSL側からコピーしてgit commit。

学生さんの論文に朱入れ。

WSLのpandocが`--shift-heading-level-by`なんてオプション知らないよ、といってきた。バージョンが古い？

```sh
$ pandoc --version
pandoc 2.5
```

うーん、Macのpandocは3.1だから古そうだなぁ。とりあえず

```sh
sudo apt update
sudo apt upgrade
```

してみる。あらためてインストールしようとしたが入らない。仕方ないので公式から最新版をダウンロードして入れる。

```sh
sudo apt-get purge --autoremove pandoc
https://github.com/jgm/pandoc/releases/download/3.1.2/pandoc-3.1.2-1-amd64.deb
sudo dpkg -i pandoc-3.1.2-1-amd64.deb
```

```sh
$ pandoc --version
pandoc 3.1.2
```

あっさり最新版になった。

講義ノートの図を作り始める。進捗がかなりヤバい。

あまりのヤバさにfaviconを作ってしまう。いや、スマホでの閲覧チェックしたら、Chromeが「favicon.icoが見つからない」とかエラー出すから・・・
