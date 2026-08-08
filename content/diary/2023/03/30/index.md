---
title: "2023年3月30日"
date: 2023-03-30T00:00:00+09:00
lastmod: 2023-03-30T00:00:00+09:00
type: diary
source_month: "d202303.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

輪講の本選び。

* 「しっかり学ぶ数理最適化 モデルからアルゴリズムまで」
  * 機械学習ではないが、面白いテーマか。ただ、初学者向きではない？
* パターン認識と機械学習
  * 定番。やっぱりこれかなぁ。
  * https://www.amazon.co.jp/dp/4621061224
* 機械学習スタートアップシリーズ ベイズ推論による機械学習入門
  * PRMLよりわかりやすいと評判。これでも良いかな。
  * https://www.amazon.co.jp/dp/4061538322
* ガウス過程と機械学習
  * これも評判良さそう。
  * https://www.amazon.co.jp/dp/4061529269/

研究室ミーティング。その後ハンズオン。今日はMarkdown+LaTeX記法。

WordPressがPHP 7.4にしろと言ってきたのをずっと放置してた。現在のバージョン。

```sh
$ php --version
PHP 7.3.4 (cli) (built: Apr  2 2019 13:48:50) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.4, Copyright (c) 1998-2018 Zend Technologies
```

これを7.4にしないといけない。サーバはCentOS 7.9.2009。そもそもサーバのディストリビューションをなんとかしないといけない、という意見にはとりあえず耳を塞ぎ、PHPだけ上げてみる。EPELでいけるといいなぁ。

```sh
sudo yum -y install epel-release
```

[ここ](http://rpms.remirepo.net/)からREMIのリポジトリを探す。`ftp.riken.jp`の、`remi-release-7.rpm`かな。

```sh
$ sudo yum -y install http://ftp.riken.jp/Linux/remi/enterprise/remi-release-7.rpm
読み込んだプラグイン:fastestmirror, langpacks, product-id, search-disabled-repos, subscription-manager

This system is not registered with an entitlement server. You can use subscription-manager to register.

remi-release-7.rpm                                                            |  27 kB  00:00:00     
/var/tmp/yum-root-jhRPU5/remi-release-7.rpm を調べています: remi-release-7.9-5.el7.remi.noarch
/var/tmp/yum-root-jhRPU5/remi-release-7.rpm: インストールされたパッケージを更新しません。
エラー: 何もしません
```

`yum search php74`で出てきたら成功。インストールしてみる。いきなりWPが動かなくなったりしませんように。

```sh
sudo yum -y install php74 php74-php 
```

インストールされたか調べる。

```sh
$ php74 --version
PHP 7.4.33 (cli) (built: Feb 14 2023 08:49:52) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies

$ php --version
PHP 7.3.4 (cli) (built: Apr  2 2019 13:48:50) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.4, Copyright (c) 1998-2018 Zend Technologies
```

php74は入ったけど、デフォルトはphp 7.3のままだなぁ。

```sh
$ which php
/usr/bin/php

$ which php74
/usr/bin/php74
```

なんかRHEL由来のサブスクリプションマネージャの問題らしい。ちゃんと登録するのが筋だろうが、面倒なので無効化してしまおう。`/etc/yum/pluginconf.d/subscription-manager.conf`の`enabled=1`を0に。その後yumをアップデート。

```sh
sudo yum clean all 
sudo yum update
```

```sh
$ php --version
PHP 7.4.33 (cli) (built: Feb 14 2023 09:31:03) ( NTS )
Copyright (c) The PHP Group
Zend Engine v3.4.0, Copyright (c) Zend Technologies
```

できた。WordPressも無事に表示されたまま。よかった。デフォルトテーマのTwenty FourteenとTwenty Twenty-Threeを削除。

あと、imagick、zip、intlがあると良いと書いてある。ImageMagickエンジンのプラグインをインストール＆有効化。

```sh
sudo yum install -y php-zip php-intl
sudo yum install -y ImageMagick-devel
sudo service httpd restart
```

ImageMagickを有効化するには`/etc/php.ini`に以下を追加。

```php
extension = imagick.so
```

うーん、サイトヘルスから表示が消えない。

```sh
$ php -a
php > if (!extension_loaded('imagick')){ echo "Not loaded";}
Not loaded
```

おっと。

```sh
sudo yum install -y php-imagick 
```

```sh
$ php -a
php > echo extension_loaded('imagick');
1
```

できた。apacheを再起動したらサイトヘルスから表示が消えた。めでたい。

うん、こんなことをやっている場合ではないんだ。知ってる。
