---
title: "2021年5月4日"
date: 2021-05-04T00:00:00+09:00
lastmod: 2021-05-04T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

`tldr`というコマンドを知った。manの表示をわかりやすくしてくれる。Macならbrewで入る。sshの説明ならこう。

```sh
$ tldr ssh

ssh

Secure Shell is a protocol used to securely log onto remote systems.
It can be used for logging or executing commands on a remote server.

- Connect to a remote server:
    ssh username@remote_host

- Connect to a remote server with a specific identity (private key):
    ssh -i path/to/key_file username@remote_host

- Connect to a remote server using a specific port:
    ssh username@remote_host -p 2222

- Run a command on a remote server:
    ssh remote_host command -with -flags

- SSH tunneling: Dynamic port forwarding (SOCKS proxy on localhost:1080):
    ssh -D 1080 username@remote_host

- SSH tunneling: Forward a specific port (localhost:9999 to example.org:80) along with disabling pseudo-[t]ty allocation and executio[n] of remote commands:
    ssh -L 9999:example.org:80 -N -T username@remote_host

- SSH jumping: Connect through a jumphost to a remote server (Multiple jump hops may be specified separated by comma characters):
    ssh -J username@jump_host username@remote_host

- Agent forwarding: Forward the authentication information to the remote machine (see `man ssh_config` for available options):
    ssh -A username@remote_host
```

おお、わかりやすい。

基礎実験。

物性研スパコンハンズオン、資料を作ったぞ。すげー時間かかった。
