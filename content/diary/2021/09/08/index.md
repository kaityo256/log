---
title: "2021年9月8日"
date: 2021-09-08T00:00:00+09:00
lastmod: 2021-09-08T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WSL2のUbuntuでpdftkを使いたい。そのためにはsnapが必要。しかし、WSL2のUbuntuではsnapdが走っていない。走らせるには[以下のようにすれば良いらしい](https://github.com/microsoft/WSL/issues/5126#issuecomment-653715201)。

```sh
sudo apt-get update && sudo apt-get install -yqq daemonize dbus-user-session fontconfig
sudo daemonize /usr/bin/unshare --fork --pid --mount-proc /lib/systemd/systemd --system-unit=basic.target
exec sudo nsenter -t $(pidof systemd) -a su - $LOGNAME
```

```sh
$ snap version
snap    2.49.2+20.04
snapd   2.49.2+20.04
series  16
ubuntu  20.04
kernel  4.19.128-microsoft-standard
```

動いた。

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

わーい、入った。
