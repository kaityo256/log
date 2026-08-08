---
title: "2024年3月7日"
date: 2024-03-07T00:00:00+09:00
lastmod: 2024-03-07T00:00:00+09:00
type: diary
source_month: "d202403.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ハンズオン。論文の読み方、探し方。

研究室ミーティング。

研究室ウェブサイトがまた「データベース接続確立エラー」。

またかと思ってmariadbを再起動したが治らない。あれ？と焦ったら、ウェブサーバではなく計算サーバにログインしてた。道理でアクセスログが全然残ってないなと思った。最近眠くて頭が全く働いてない。

```txt
240307 14:18:34 mysqld_safe Number of processes running now: 0
240307 14:18:39 mysqld_safe mysqld restarted
240307 14:18:48 [Note] /usr/libexec/mysqld (mysqld 5.5.68-MariaDB) starting as process 30844 ...
240307 14:18:49 InnoDB: The InnoDB memory heap is disabled
240307 14:18:49 InnoDB: Mutexes and rw_locks use GCC atomic builtins
240307 14:18:49 InnoDB: Compressed tables use zlib 1.2.7
240307 14:18:49 InnoDB: Using Linux native AIO
240307 14:18:49 InnoDB: Initializing buffer pool, size = 128.0M
240307 14:18:50 InnoDB: Completed initialization of buffer pool
240307 14:18:50 InnoDB: highest supported file format is Barracuda.
InnoDB: The log sequence number in ibdata files does not match
InnoDB: the log sequence number in the ib_logfiles!
InnoDB: Restoring possible half-written data pages from the doublewrite buffer...
240307 14:18:57 mysqld_safe mysqld from pid file /var/run/mariadb/mariadb.pid ended
```

なんかデータベースの不整合が起きて、その復旧をしようとして死んだ、という感じですかね。

`ps aux | grep mysql`しても出てこないので死んでますな。

```sh
sudo service mariadb restart
```

で起動。

なんか今日の14:18にmysqldが再起動して、不整合で死んだ感じだな。

アクセスログを調べたが、そのあたりで攻撃を受けている(例えばコマンドインジェクション)のは間違いないが、成功はしておらず、他に怪しいログは見当たらない。なんで死んだんだろう？

いくつかTodoをこなしたら時間切れ。
