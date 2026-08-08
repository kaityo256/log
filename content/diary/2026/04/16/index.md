---
title: "2026年4月16日"
date: 2026-04-16T00:00:00+09:00
lastmod: 2026-04-16T00:00:00+09:00
type: diary
source_month: "d202604.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

計算ノードがNISクライアントにならない。無事なノードも

```txt
RPC: Unable to receive; errno = No route to host
```

と出るので、RPCによる通信に失敗しており、新規のNISクライアントが受付られていなさそう。

* ログインノードからsshは通る

```sh
$ rpcinfo -p 192.168.1.10
   program vers proto   port  service
    100000    4   tcp    111  portmapper
    100000    3   tcp    111  portmapper
    100000    2   tcp    111  portmapper
    100000    4   udp    111  portmapper
    100000    3   udp    111  portmapper
    100000    2   udp    111  portmapper
    100004    2   udp    887  ypserv
    100004    1   udp    887  ypserv
    100004    2   tcp    887  ypserv
    100004    1   tcp    887  ypserv
```

```sh
$ nc -vz 192.168.1.10 887
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: No route to host.

$ nc -vz 192.168.1.10 111
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Connected to 192.168.1.10:111.
Ncat: 0 bytes sent, 0 bytes received in 0.01 seconds.
```

うん、111は通るけど、887が駄目ですね。

サーバ側で開ける。

```sh
firewall-cmd --permanent --add-port=887/tcp
firewall-cmd --permanent --add-port=887/udp
firewall-cmd --reload
```

クライアントで確認。

```sh
$ nc -vz 192.168.1.10 887
Ncat: Version 7.92 ( https://nmap.org/ncat )
Ncat: Connected to 192.168.1.10:887.
Ncat: 0 bytes sent, 0 bytes received in 0.01 seconds.
```

通った。ypservが使うポートが起動するたびに変わるのが原因だった。

計算ノードでypbindが起動したが、まだNISを認識しない。これは`/etc/nsswitch.conf`の順序が問題だった。passwd, group, shadowに対してnisを有線するように書き換えて

```sh
sudo systemctl restart ypbind
```

してからログインしなおしたらうまくいった。まとめると、

* ypservが起動の度に異なるポートを使う設定になっていた
* 計算ノードがメモリ枯渇で死亡。この時、ypbindも死亡。
* つながらない原因を調べるため、ログインノードを再起動。このせいでypservが異なるポートを掴む
* 計算ノードはログインノードが指定するポートで通信しようとするが、計算ノードのファイアウォールのせいで通信できずNISクライアントになれなかった。

つまり、計算ノードのypbindが死んだだけなら計算ノードの再起動でうまくいくはずだったが、ログインノードを再起動したために新たな問題を持ち込み、その切り分けができていなかった。

これ、正しい実装は、計算ノード側でypservが使うポートを固定することなんだけど、これやると全部再起動になって面倒だな・・・次の停電の時の対応にしよう(忘れそう)。

というわけで計算ノードを復帰。

```sh
sudo scontrol update NodeName=yagami01.appi.keio.ac.jp State=RESUME
```

```sh
$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
main*        up 1-00:00:00      3   idle yagami01.appi.keio.ac.jp,yagami02.appi.keio.ac.jp,yagami03.appi.keio.ac.jp
```

復帰した！一週間かかったぞ。

結局、問題はログインノードのファイアウォールだったのだが、「ypservが起動するたびに異なるポートを掴むという仕様を知らなかった」「他のノードは無事だったのでログインノードを疑わなかった」のが原因究明を阻んだ。NISクライアントとして掴む時だけそのポートを使い、後は使わないので、一度NISクライアントになったノードはポートが移ってもNISクライアントであり続ける。

さすがにNISは卒業しないとだめか。でもLDAP面倒くさい・・・

研究室ミーティング。超新星爆発におけるRT不安定性と、チェスパズルの難易度推定。どちらも興味深かったです。

眠くて死んでしまう。
