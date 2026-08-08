---
title: "2022年2月25日"
date: 2022-02-25T00:00:00+09:00
lastmod: 2022-02-25T00:00:00+09:00
type: diary
source_month: "d202202.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

大きなディスプレイが納品された。

新しいiMacに移動。Dog Fooding。

日本語。変換「前」に候補がでるMacデフォルトのやつ(ことえり?)がどうしても苦手なので、Google日本語入力をインストール。

Thunderbirdはプロファイルのフォーマットが変わっていたためにできず。諦めてアカウントを設定したら普通にimapでそのまま読めた。ローカルファイルだけscp。

まず、Mendeleyをインストール。AppStoreに紛らわしい「Mendeley Web Importer」というのがあって、間違えて入れてしまった。

VSCodeをインストール。

Pythonのインストール。

```sh
python3 -m pip install --upgrade pip
python3 -m pip install ipython 
```

あと、頻繁にログインするサーバに公開鍵を登録する作業。研究室計算サーバ、研究室ウェブサーバ、物性研、名大につないだ。

ChromeにNew tab redirectを入れた。LastPassは最初に入れてある。

Slack入れた。研究室と大学、その他。

ハンズオンの準備。

```sh
docker pull ubuntu
```

をしたら、

```txt
Error response from daemon: Get "https://registry-1.docker.io/v2/": net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
```

みたいなエラー。

英語検索のために`https://www.google.com/?hl=en&gws_rd=cr`をブックマーク。

Dockerをリスタート。

```sh
sudo service docker restart
```

だめ。

Macでdockerを入れる。

```sh
brew install docker
```

Docker Desktopもインストール＆起動。

最終的に、`/etc/resolv.conf`に

```txt
nameserver 8.8.8.8
```

を追加したらいけた。nameserverの問題？

CentOSでネットがいちいち遅い。ipv6の問題かもしれないため無効にしてみる。

`/etc/sysctl.conf`に`net.ipv6.conf.all.disable_ipv6 = 1`を追記して、

```sh
sysctl -p
```

を実行。`ifconfig |grep inet6`を実行して消えたことを確認。

だめだ。まだ遅い。間違いなくなにかタイムアウトしている。

`/etc/resolv.conf`のデフォルトのやつを消して`8.8.8.8`だけにしたら早くなった。DNSのタイムアウトか。

Dockerハンズオン完走。これで月曜日はよし。

そうか、Dockerのエラーがわかった。DNSでプライマリにたずねてタイムアウトするまでに、Dockerが諦めちゃうんだ。curlとかだとタイムアウトしないのでつながらないのがわからなかった。

一応[Zennのスクラップ](https://zenn.dev/kaityo256/scraps/c335ac8c76c5e1)に書いておいた。

あ、brew入ってなかった。

```sh
brew install wget
```

あー、でもcurlでやってみるか。

MacへのTexLiveのインストール。

```sh
cd build
curl -O http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet/install-tl-unx.tar.gz
tar xvzf install-tl-unx.tar.gz
```

lab_startupのVimの終了についても書いた。

論文には全く取りかかれなかったが、それなりに仕事はできたのではないか。
