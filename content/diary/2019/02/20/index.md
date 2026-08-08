---
title: "2019年2月20日"
date: 2019-02-20T00:00:00+09:00
lastmod: 2019-02-20T00:00:00+09:00
type: diary
source_month: "d201902.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Google Chromeの履歴で、条件にマッチしたものを削除したかった。
履歴ファイルはSQLite形式なので、Rubyから叩こうかと思ったが、結局それくらいなら直接sqlite3からいけると思ってやらんかった。

sqlite3で正規表現を使おうとして、sqlite-develを入れてから、[https://github.com/ralight/sqlite3-pcre](https://github.com/ralight/sqlite3-pcre)を苦労してビルドしたりした(デフォルトではmakeできない)が、結局LIKE文でいけた。

覚書をQiitaに書いておいた。→[Google Chromeで条件にマッチした履歴を削除](https://qiita.com/kaityo256/items/dd306110580100159041)
