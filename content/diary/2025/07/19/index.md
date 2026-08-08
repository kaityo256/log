---
title: "2025年7月19日"
date: 2025-07-19T00:00:00+09:00
lastmod: 2025-07-19T00:00:00+09:00
type: diary
source_month: "d202507.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

修論中間発表。皆さんちゃんとできて良かった。

家のPCのUbuntuが古く、aptで入るGoが古い。そのせいで、ooxgrepが使えない。

```sh
wget -q https://go.dev/dl/go1.24.5.linux-amd64.tar.gz 
sudo tar -C /usr/local -xvf go1.24.5.linux-amd64.tar.gz  
export PATH=$PATH:/usr/local/go/bin 
export PATH=$PATH:~/go/bin
go install github.com/kaityo256/ooxmlgrep@latest
```

```sh
$ ooxmlgrep 

Options:
  -n, --number        Show slide number only (like grep -n)
  -i, --ignore-case   Ignore case distinctions
  --version           Show version and exit
```

できた。
