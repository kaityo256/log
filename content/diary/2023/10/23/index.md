---
title: "2023年10月23日"
date: 2023-10-23T00:00:00+09:00
lastmod: 2023-10-23T00:00:00+09:00
type: diary
source_month: "d202310.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

1on1 x 3。

会議。

物理情報工学ソフトウェア開発演習第二回。

ChatGPTの更新ができなかったのだが、今日もう一度トライしたらなぜかできた。Grammarlyのカードの更新が拒否される。なぜだ。

研究室のWordPressが落ちてる。「データベース接続確立エラー」と表示される。

ChatGPTに質問しながら問題を確認する。MySQLの接続確認。

```sh
$ mysql -h ホスト名 -u ユーザ名 -p
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (111)
```

MySQLサーバが動いていないっぽい。`/etc/my.cnf`を調べる。

```txt
[mysqld_safe]
log-error=/var/log/mariadb/mariadb.log
pid-file=/var/run/mariadb/mariadb.pid
```

MySQLではなくMariaDBを使っている。調べたらMySQLからMariaDBが派生したらしい。

エラーログを調べる。

```sh
231021  1:01:03 Percona XtraDB (http://www.percona.com) 5.5.61-MariaDB-38.13 started; log sequence number 2160461709
231021  1:01:04 [ERROR] mysqld: Out of memory (Needed 128917504 bytes)
231021  1:01:05 [Note] Plugin 'FEEDBACK' is disabled.
231021  1:01:08 [Note] Server socket created on IP: '0.0.0.0'.
231021 01:01:11 mysqld_safe mysqld from pid file /var/run/mariadb/mariadb.pid ended
```

メモリ不足で落ちてる。その前に執拗な攻撃を受けていたので、それだろうか。

再起動する。

```sh
sudo service mariadb restart
```

復活した。焦った。

定期的なバックアップを取らなければ・・・(と思いつつまた何もしない)

うごわ！明日までのレポートの採点忘れてる！

* 21:33 採点開始
* 22:25 採点終了
