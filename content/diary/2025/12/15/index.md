---
title: "2025年12月15日"
date: 2025-12-15T00:00:00+09:00
lastmod: 2025-12-15T00:00:00+09:00
type: diary
source_month: "d202512.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

なんか、善意で公開しているものについて上から目線で「コメント」が来るとイラッとするな。うーん。

Macの更新がくるたびにクリーンインストールする、という話を聞いて「えぇ……」と思っていたのだが、Windows PCを一度クリーンインストールしてからの復活が結構早かった。よく考えたら、必要なデータが全てクラウドにあるから、バックアップが不要で開発環境だけでいいんだな。かつ、開発環境はaptかbrewで入るから、復活が早い。

っていうか、だいぶスッキリしたから、数カ月に一度はクリーンインストールしても良いかもしれない。

というわけで手元のMacも、ローカルデータをなるべく削除。いつでもクリーンインストールできる状態を目指す。

これまで学科のメールはGMailからpopで読んでいたが、GMailがサードパーティ制のPOPのサポートを止めるということで、keioアカウントに転送するようにした。もともとGMailのPOPはそれなりの頻度で確認が走っていたのが、だんだん間隔があいていき、現在は1時間〜1時間半に一度になり、わざわざ設定から「新しいメールをチェック」をしないといけなくなっていたので不便だった。「先程送ったメールですが」というSlackの通知で慌ててメールを読みにいく、とかやっていた。これからはすぐメールが読めるようになるはず(そうすると仕事も増えそうだが)。

実験レポート採点した。

某書類提出した(←日記としては意味をなさない記述だが、いろいろやったのだ、という自己満足の記録)。

計算ノードが死んでいる。

```sh
$ sinfo
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
main*        up 1-00:00:00      1  drain yagami03.appi.keio.ac.jp
main*        up 1-00:00:00      1  alloc yagami01.appi.keio.ac.jp
main*        up 1-00:00:00      1   down yagami02.appi.keio.ac.jp
```

yagami01-03のうち、yagami02がdown、yagami01がdrainになっている。

```sh
$ sinfo -R
REASON               USER      TIMESTAMP           NODELIST
Duplicate jobid      slurm     2025-12-13T08:17:44 yagami03.appi.keio.ac.jp
Node unexpectedly re slurm     2025-12-11T17:09:42 yagami02.appi.keio.ac.jp
```

yagami02が管理を外れた原因は明確で、unexpectedly rebootedだな。yagami02はゾンビジョブがあったため、手で再起動したのだが、それがSlurmによる予期しない再起動となった。

```sh
sudo scontrol update NodeName=yagami02.appi.keio.ac.jp State=RESUME
```

で復活した。次からは

```sh
sudo scontrol update NodeName=yagami02.appi.keio.ac.jp State=DRAIN Reason="maintenance reboot"
```

などとしてから再起動して

```sh
sudo scontrol update NodeName=yagami02.appi.keio.ac.jp State=RESUME
```

とすればOK。

yagami03はゴミが残っている模様。

まずslurmdを止める。

```sh
ssh yagami03
sudo systemctl stop slurmd
```

```sh
$ ls /var/spool/slurm/d
cred_state  cred_state.old  hwloc_topo_whole.xml
```

余計なファイルを削除

```sh
sudo rm cred_state cred_state.old hwloc_topo_whole.xml
```

slurmd再起動。

```sh
sudo systemctl start slurmd
```

ログインノードに戻って

```sh
sudo scontrol update NodeName=yagami03.appi.keio.ac.jp State=RESUME
```

復活した。やれやれ。

こういうのはChatGPT強いなぁ。

頼まれ原稿に手をつける時間がまったくとれない上に、さらに査読x2が降ってきた。うげ。

Google Chrome、大学のアカウントだとWeb Storeが使えないのか。

新しいタブを開いたときにいろいろでて困る場合は「Chromeをカスタマイズ」から「ショートカット」の「ショートカットを表示」をオフ、「カード」の「カードを表示」をオフにすればOK。みられるとあまりよろしくないファイル名とかあるから困る。

学校のPCだとWSLgが問題なく走ったけど、家のPCだと動かんなぁ。

PowerShellでバージョン確認。

```sh
wsl --version
WSL バージョン: 2.6.2.0
カーネル バージョン: 6.6.87.2-1
WSLg バージョン: 1.0.71
MSRDC バージョン: 1.2.6353
Direct3D バージョン: 1.611.1-81528511
DXCore バージョン: 10.0.26100.1-240331-1435.ge-release
Windows バージョン: 10.0.26200.7462
```

最新だよな。

```sh
wsl --update
wsl --shutodwn
```

してからxeyesしたらうまくいった。なんやねん。

新しいUbuntu、いつのまにかデフォルトでopenコマンドが入ってる。
