---
title: "2019年9月14日"
date: 2019-09-14T00:00:00+09:00
lastmod: 2019-09-14T00:00:00+09:00
type: diary
source_month: "d201909.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

GitHub Actionのテストのために、ローカルにDockerを入れる。WindowsにDocker-CEを入れるには、まずDockerアカウントを作る必要がある。それをインストール。また、WSLにもDockerをインストール。WindowsはHyper-Vを有効にして再起動する必要がある。また、Docker for WindowsでExposeなんとかでサーバを見えるようにする。そして、WSL側で

```sh
export DOCKER_HOST=tcp://localhost:2375
```

とすれば、WSLでDockerが使えるようになる。

GitHub ActionsでUbuntu 18.04を使うが、どうせlatestと同じなのでlatestをひっぱる。

```sh
docker pull ubuntu
```

入ったことを確認。

```sh
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              latest              a2a15febcdf3        4 weeks ago         64.2MB
```

起動。

```sh
$ docker run -it ubuntu /bin/bash
root@f18b2a95711e:/# apt update
root@f18b2a95711e:/# apt install -y pandoc
```

で入ることを確認。

Dockerでファイルを共有するには、Docker側でShared Driveで共有するドライブにチェックを入れる必要がある。

とりあえず、Desktopにgithub\\actions_testを

```sh
docker run  -v c:\\Users\\watanabe\\Desktop\\github\\actions_test:/temp ubuntu ls /temp
```

```sh
docker run  -it -v c:\\Users\\watanabe\\Desktop\\github\\actions_test:/temp ubuntu /bin/bash
apt update
apt install -y pandoc
pandoc -s README.md -o test.html -t html --template=template
```

できた。
