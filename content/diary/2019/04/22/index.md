---
title: "2019年4月22日"
date: 2019-04-22T00:00:00+09:00
lastmod: 2019-04-22T00:00:00+09:00
type: diary
source_month: "d201904.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

さくらにVPSサーバを立てた。

* とりあえずPermitRootLoginをno
* ユーザ作成
* httpdのインストール
* /etc/httpd/conf.d/security.confで

```conf
ServerTokens Prod
```

* dockerのインストール

```sh
sudo yum install docker
```

* Pythonのインストール

```sh
sudo yum install python36 python36-pip
sudo ln -s /usr/bin/pip3.6 /usr/local/bin/pip
sudo /usr/local/bin/pip install pipenv 
```

* dockerファイルの場所でpipenvする

```sh
mkdir www
cd www
# docker-compose.ymlを作成
pipenv install docker-compose
pipenv shell
```

docker-compose upしてみる。

```sh
$ docker-compose up
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?

If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
(www)
```

dockerのパーミッションが足りない。sudoでやりたくなければ、ユーザをdockerグループに所属させる。

```sh
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo systemctl restart docker
```

一度ログアウトして、再度ログインするとdocker-compose upできるようになる。
しかし、mysqlに接続できない。firewallにmysqlを追加する。

```sh
sudo firewall-cmd --add-service=mysql --zone=public --permanent
```

だめだ。やりなおし。

```sh
mv www www2
mkdir www
cd www
docker pull mysql:5.7.21
docker pull wordpress
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=test-pw -d mysql:5.7.21
docker run --name test-wordpress --link test-mysql:mysql -d -p 8080:80 wordpress
```

だめだ。どうしてもデータベースにアクセスできない。まずローカルで試すか。

```sh
brew install docker
brew cask install docker
open /Applications/Docker.app
```

このあと、docker psが帰ってくるまでまつ。

```sh
mkdir www
cd www
docker pull mysql:5.7.21
docker pull wordpress
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=test-pw -d mysql:5.7.21
docker run --name test-wordpress --link test-mysql:mysql -d -p 8080:80 wordpress
```

run時にイメージがなかったらどうせダウンロードしてくれるから、docker pullいらんかったな。
うーん、ローカルではあっさり動いたなぁ。

もう一度さくらでやったらあっさり動いた。何がわるかったんだ？mysqlのポートか？
