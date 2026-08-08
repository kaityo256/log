---
title: "2021年9月10日"
date: 2021-09-10T00:00:00+09:00
lastmod: 2021-09-10T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

certbotがエラーを出している。

```txt
Your system is not supported by certbot-auto anymore.
```

ログインして確認。

```sh
$ sudo certbot renew --dry-run
(snip)
All renewal attempts failed. The following certs could not be renewed:
(snip)
```

おっと。なんかバージョンが古いのが問題らしい。

```sh
$ certbot --version
certbot 0.31.0
```

バージョンをあげてみる。

```sh
yum install --enablerepo=epel certbot
```

```sh
$ certbot --version
An unexpected error occurred:
AttributeError: 'module' object has no attribute 'TLSSNI01'
Please see the logfile '/tmp/tmpjRf06l/log' for more details.
```

うげ、バージョンを上げたら動かなくなったぞ。python2-certbotをアップデートすれば良いらしい。

```sh
sudo yum update python2-certbot*
```

```sh
$ certbot --version
certbot 1.11.0
```

よしよし、動いた。

```sh
$ sudo certbot renew --dry-run
(snip)
Congratulations, all simulated renewals succeeded:
```

動いた。よかった。焦った。
