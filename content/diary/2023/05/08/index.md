---
title: "2023年5月8日"
date: 2023-05-08T00:00:00+09:00
lastmod: 2023-05-08T00:00:00+09:00
type: diary
source_month: "d202305.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

さて、講義準備をしなくては。

[中年男性のツイッターでのつぶやきが苦手なんだけど変？](https://anond.hatelabo.jp/20230507164100)

これ、中年男性側の気持ちがものすごくわかる。独り言のようでいて、反応が欲しそうな「チラッチラッ」感、出しちゃうよね。「この前、大江健三郎を再読したんだけどやっぱり読みにくいんだよな」みたいな独り言を書いた時、そこに「いいね」がつくことで、自分以外にもそう思った人がいる、という安心感が欲しいんだよね。ただ、そういう気持ちが悍ましいという気持ちもわかる。両方わかる。

そういう意味では、ここのlogが本当の意味での独り言だな。コメントだのトラックバックだのSNSボタンだのが全くついていない。

全く反応を期待していないブログをなぜ公開するか、というのは、わりと昔から一貫している。すなわち「今日、自分がこういうことを考えた、ということを、他の誰かが知っている(かもしれない)、という事実が欲しいから」。このlogを読んだ人は、僕の考えに触れ、そしてそれをすぐに忘れるだろう。しかし、数日後、数カ月後、数年後に、なにかの考えが浮かんだ時、実はそれがこのlogで読んだことを「自分で思いついた」と思って「思い出す」かもしれない。こうすることで、僕の思考は世の中に拡散し、生き残っていく。

一方、SNSでなにかを発信すると、反応はつくんだけど、どちらかというと「情報が生き残る」というよりは「情報が消費される」という印象の方が強い。

ブログ、M2の頃から書きはじめたんだよな。当時はいろいろ悩んでて、その悩みを赤裸々に書いていた。記録によると2000年7月23日から2019年1月10日まで書いている(途中から非公開にしていた？記憶がない)。しかし18年ってすごいな。ただし、最後の数ヶ月はほとんど書いていない。

よく考えると、いま自分が「先生」と読んでいる人が修士や博士の頃にどんなことをして、どんなことを考えていたのかがわかるのか。それはそれで貴重な資料ですね。公開するつもりはないけど。昔の日記に貼ってたランダムメッセージくらいサルベージしてもいいかなぁ。

昔の自分の日記を読み始めたら止まらなくなった。この「掃除中にアルバムを見つけてしまった」感。このlogはあまり感情をあらわにしていないので、読み返してもさほど面白くはないですね。

研究室サーバのIntel Compilerがライセンスサーバにつながらずに動かなくなっている。

まずライセンスファイルを確認。

```txt
SERVER servername hogehoge ポート番号
USE_SERVER
```

このポート番号が開いてるか調べる。

```sh
$ sudo netstat -anp  |grep ポート番号
tcp6     129      0 :::ポート番号                :::*                    LISTEN      4385/lmgrd 
```

lmgrdが起動し、指定のポート番号をLISTENしてる。

```sh
ps aux |grep lmgrd 
```

これで、どのlicファイルを読み、どのログファイルに吐いているかを確認。

```sh
$ sudo ./lmdown -c /path/to/file.lic
lmdown - Copyright (c) 1989-2018 Flexera. All Rights Reserved.
Shutdown failed: Cannot read data from license server system. (-16,287)
```

ログを見る。

```txt
10:22:01 (INTEL) SERVER-OUT: Failed to send the message(71) <END>
10:22:01 (INTEL) Lost connection to lmgrd, heartbeat timeout expired, exiting.
10:22:01 (INTEL) Heartbeat timeout is 300 seconds. Elapsed time is 715 seconds.
10:22:01 (INTEL) EXITING DUE TO SIGNAL 37 Exit reason 5
10:22:01 (INTEL) IN: "IC45FB71A" user@server.name  (SHUTDOWN)
10:22:01 (INTEL) IN: "Comp-CL" user@server.name  (SHUTDOWN)
```

なんかheartbeatタイムアウトで死んでる。仕方ない。まず、

```sh
sudo ps aux | grep lmgrd
```

でlmgrdの起動オプション、特にライセンスファイルとログ・ファイルの位置を確認しておく。

killする。普通にkillできなかったので-KILL。

```sh
sudo kill -KILL 4385 
```

lmgrdの再起動。

```sh
sudo /opt/intel/licenseserver/lmgrd -c /path/to/file.lic -l /path/to/log.txt
```

```sh
$ icpc
icpc: command line error: no files specified; for help type "icpc -help"
```

インテルコンパイラが起動するようになった。やれやれ。

ログインノードの情報を表示。

```sh
$ qmgr -c "p n name_of_server"
#
# Create nodes and set their properties.
#
#
# Create and define node watanabe-login
#
create node name_of_server Mom=name_of_server.host.name
set node name_of_server state = free
set node name_of_server resources_available.arch = linux
set node name_of_server resources_available.host = name_of_server
set node name_of_server resources_available.mem = 97375328kb
set node name_of_server resources_available.ncpus = 40
set node name_of_server resources_available.vnode = name_of_server
set node name_of_server queue = workq
set node name_of_server resv_enable = True
```

ログインノードにジョブを投入できないようにしたらジョブがエラーで死ぬ。何が原因かしばらくわからなかったが、そもそも他のノードにジョブがディスパッチできない。/homeがマウントされていないのが原因。まじか。

これ、/homeもそうだけど、そもそもNISが通ってないのが原因。いつのまにか死んでいたらしい。ログインノードへのディスパッチの優先順位を下げたら、ジョブを投入したら死ぬようになったと思っていたが、最初からログインノード以外にジョブがディスパッチされたら死ぬ状態だったようだ。PBSがらみのエラーだと思って原因究明が遅れてしまった。

しかし、面倒だなぁ……
