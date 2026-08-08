---
title: "2019年4月23日"
date: 2019-04-23T00:00:00+09:00
lastmod: 2019-04-23T00:00:00+09:00
type: diary
source_month: "d201904.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

さくらVPSにWordpressを入れる。

```sh
sudo yum install httpd mysql-server php php-mysql wget
sudo yum install mariadb mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
mysql -u root
MariaDB [(none)]> update mysql.user set password=password('rootパスワード入力') where user = 'root';
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> exit;
# mysql -u root -p
# Enter password:
MariaDB [(none)]> create database wordpress;
MariaDB [(none)]> show databases;
MariaDB [(none)]> exit;
```

```sh
mkdir build
cd build
wget https://ja.wordpress.org/latest-ja.zip
unzip latest-ja.zip
```
