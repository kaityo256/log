---
title: "2019年4月25日"
date: 2019-04-25T00:00:00+09:00
lastmod: 2019-04-25T00:00:00+09:00
type: diary
source_month: "d201904.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

CentOS7にPHP7を入れる。

```sh
$ sudo  yum install epel-release
パッケージ epel-release-7-11.noarch はインストール済みか最新バージョンです
何もしません
```

EPELは入ってた。次はRemi。

```sh
sudo yum -y install http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
```

PHPのリポジトリが入ってるか確認。

```sh
$ ls -l /etc/yum.repos.d | grep php
-rw-r--r--  1 root root  456  3月  8 16:34 remi-php54.repo
-rw-r--r--  1 root root 1314  3月  8 16:34 remi-php70.repo
-rw-r--r--  1 root root 1314  3月  8 16:34 remi-php71.repo
-rw-r--r--  1 root root 1314  3月  8 16:34 remi-php72.repo
-rw-r--r--  1 root root 1314  3月  8 16:34 remi-php73.repo
```

入ってた。php5を消してからphp73を入れよう。

```sh
sudo yum remove remove php php-*
sudo yum install --enablerepo=remi,remi-php73 php php-mysql php-mbstring php-gd
```

どれが必要なのかわからなかったので、とりあえず必要そうなもの全部指定。

次、WordPressのCocoonテーマを入れてみる。

[https://wp-cocoon.com/downloads/](https://wp-cocoon.com/downloads/)の「Cocoonテーマ」から
親テーマと子テーマをダウンロード。[https://wp-cocoon.com/theme-install/](https://wp-cocoon.com/theme-install/)の手順に従って入れる。

そうしたら「アップロードしたファイルは php.ini で定義された upload_max_filesize を超過しています。」とと文句を言われたので、`/etc/php.ini`の当該項目を

```ini
upload_max_filesize = 8M
```

に修正。できた。あとはCSSを修正しながら様子を見る感じで。
