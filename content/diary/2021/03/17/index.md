---
title: "2021年3月17日"
date: 2021-03-17T00:00:00+09:00
lastmod: 2021-03-17T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室サーバでDockerを使おうとしたら

```txt
Error response from daemon: Get https://registry-1.docker.io/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
```

と言われて死んでいる。どうしよう？

`etc/resolv.conf`に

```txt
nameserver 8.8.8.8
```

を追加したら通った。デフォルトのnameserverがおかしい？

明日のDockerハンズオンの準備完了。

明日のもう一つのスライド作った。SIMDのクラスターアルゴリズムについて。


木曜日の発表の準備。スケーリング次元とか完全に忘れてた。
