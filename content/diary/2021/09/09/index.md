---
title: "2021年9月9日"
date: 2021-09-09T00:00:00+09:00
lastmod: 2021-09-09T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

本の購入。

プレ技の発表練習。輪講。一冊読み終わった。素晴らしい。そして浸透圧について何もわかっていなかったことがわかった。

なんか呆然としてしまって、手が動かないぞ。

学校のPCにsnapを入れる確認。

```sh
$ which snap
/usr/bin/snap
```

snapはデフォルトで入っている。しかし、そのままでは返答しない。

```sh
snap --version # 処理が返ってこない。
```

というわけでsnapを入れる。まだ時間が遅れてたので、まず直す。

```sh
sudo hwclock -s
```

daemonize dbus-user-session fontconfigの三つをインストール。

```sh
sudo apt-get update
sudo apt-get install -yqq daemonize dbus-user-session fontconfig
```

demonizeを起動。

```sh
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
```

snapが返事をするようになる。

```sh
$ snap version
snap    2.48.3+20.04
snapd   2.48.3+20.04
series  16
ubuntu  20.04
kernel  4.19.128-microsoft-standard
```

ログインしていないと、listなどが見られない。

```sh
$ snap list
error: access denied (try with sudo)
```

sudoを試せと言ってくるが、listを見るにはroot権限は不要で、ログインが必要。この状態でsudoしてもダメと言われる。

```sh
$ sudo snap list
error: access denied (see 'snap help login')
```

ログインしようとしたら以下のコマンドで死ぬ。

```sh
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

調べてみると、systemdが二つ動いている。

```sh
$ pidof systemd
32692 30864
```

ssh-agentはたくさん動いてる。

```sh
$ pidof ssh-agent
33686 33657 33572 32677 29135 28925 27485 24655 24530 23881 16910 10516 13
```

再起動してみるかな。PowerShellから

```sh
wsl --shutdown
```

を実行。

```sh
$ pidof ssh-agent
16
$ pidof systemd

```

ssh-agentが一つ、systemdは動いていない状態になった。demonizeでsystemdを起動。

```sh
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
```

```sh
$ pidof systemd
262
```

うん、一つになった。snapにログインする。

```sh
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

できた。

```sh
$ snap list
Name    Version   Rev    Tracking       Publisher   Notes
core18  20200707  1880   latest/stable  canonical✓  base
lxd     4.0.2     16558  4.0/stable/…   canonical✓  -
snapd   2.45.2    8542   latest/stable  canonical✓  snapd
```

実行できた。

```sh
$ snap search pdftk
pdftk  2.02-4   smoser     -      command-line tool for working with PDF files
```

pdftkを見つけた。インストールする(rootが必要)。

```sh
sudo snap install pdftk
```

```sh
$ pdftk --version

pdftk 2.02 a Handy Tool for Manipulating PDF Documents
Copyright (c) 2003-13 Steward and Lee, LLC - Please Visit: www.pdftk.com
This is free software; see the source code for copying conditions. There is
NO warranty, not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

無事に入ったぞ。よかった。

[WLS2のUbuntuでsystemdを使う](https://qiita.com/matarillo/items/f036a9561a4839275e5f)。

unshareにより、隔離された名前空間でデーモンとなるので、nsenterでその中に入る。
