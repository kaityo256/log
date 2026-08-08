---
title: "2022年2月26日"
date: 2022-02-26T00:00:00+09:00
lastmod: 2022-02-26T00:00:00+09:00
type: diary
source_month: "d202202.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室サーバ、ログインサーバでも計算できる仕組みなので、使いたいときに重いときがある。とりあえず別サーバでdockerできるようにする。

```sh
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum makecache fast
sudo yum -y install docker-ce
sudo systemctl start docker
```

次にdockerグループにパスワードを設定。

```sh
sudo gpasswd docker
```

2つほどサーバにdocker入れて動作確認した。
