---
title: "2021年7月30日"
date: 2021-07-30T00:00:00+09:00
lastmod: 2021-07-30T00:00:00+09:00
type: diary
source_month: "d202107.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室サーバでPBSが死んだ。qstatができない。

```sh
$ qstat
Connection refused
qstat: cannot connect to server watanabe-login (errno=111)
```

とりあえず

```sh
/etc/init.d/pbs start
```

で復活させたが、MPIも死んでいるらしい。研究室サーバでMPIを使おうとするとこんな感じのエラーを吐く。

```sh
$ mpirun -np 2 ./a.out
PMIX ERROR: OUT-OF-RESOURCE in file gds_dstore.c at line 1178
PMIX ERROR: OUT-OF-RESOURCE in file gds_dstore.c at line 1313
PMIX ERROR: OUT-OF-RESOURCE in file gds_dstore.c at line 2331
PMIX ERROR: OUT-OF-RESOURCE in file gds_dstore.c at line 3148
PMIX ERROR: OUT-OF-RESOURCE in file gds_dstore.c at line 3180
PMIX ERROR: OUT-OF-RESOURCE in file server/pmix_server.c at line 2170
```

原因不明。ググってもよくわからなかったので再起動をかけたらいけた。

査読依頼が来たが、ちょっと分野が違うのでちゃんとしたプロを推薦した。

研究室見学(オンライン)。今年二人目。がんばって良い研究室を探してくださいまし。

昨日の研究室ミーティングの録画を編集してアップロード。欠席者向けに。

すごく重い仕事をなんとかこなした。結構時間かかった・・・
