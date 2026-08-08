---
title: "2018年12月1日"
date: 2018-12-01T00:00:00+09:00
lastmod: 2018-12-01T00:00:00+09:00
type: diary
source_month: "d201812.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

CentOSにdockerを入れる。<a href="https://docs.docker.com/install/linux/docker-ce/centos/">公式の手順</a>に沿うだけ。

```sh
$ sudo yum remove docker \
                  docker-client \
                  docker-client-latest \                   
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
$ sudo yum install -y yum-utils device-mapper-persistent-data lvm2 
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ sudo yum-config-manager --enable docker-ce-test 
$ sudo yum install docker-ce  
$ sudo systemctl start docker 
$ sudo docker run hello-world
$ sudo systemctl enable docker
```
