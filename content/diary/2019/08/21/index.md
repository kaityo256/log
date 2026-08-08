---
title: "2019年8月21日"
date: 2019-08-21T00:00:00+09:00
lastmod: 2019-08-21T00:00:00+09:00
type: diary
source_month: "d201908.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

さくらのサーバ、Dockerを最新版にした。

[ここ](https://docs.docker.com/install/linux/docker-ce/centos/)に記述に従って、以下を順番に実行しただけ。

```sh
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine
```

```sh
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```

```sh
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

```sh
$ sudo yum install docker-ce docker-ce-cli containerd.io
$ sudo systemctl start docker
$ docker --version
Docker version 19.03.1, build 74b1e89
```

DockerのCommunity Edition (Docker-CE)が入った。

本当はDocker環境でLLVMいれていろいろためそうと思ったんだけど、やっぱり面倒になったのでそのままclangいれた。

```sh
sudo yum -y install clang
```
