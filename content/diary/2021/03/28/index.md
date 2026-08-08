---
title: "2021年3月28日"
date: 2021-03-28T00:00:00+09:00
lastmod: 2021-03-28T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

いまいち体調が良くない。履修案内を読み込む。いろいろ知らなかった。

Ubuntu 18.04のGitのバージョンが古く、デフォルトブランチをmainにできないため、Ubuntuのバージョンを上げることに。

WSL2 のUbuntuを18.04から20.04に。[ここ](https://qiita.com/hitobb/items/2ee9b1c2c49760976e0f)を参考に。

```sh
sudo apt update
sudo apt upgrade
sudo apt install update-manager
sudo apt dist-upgrade
sudo do-release-upgrade -d
```

```sh
$ git --version
git version 2.25.1
```

うーん、gitのバージョンが2.28に届かなかった。当面はいいことにするか。

今週のGitハンズオンの準備はした。だが、ブランチの説明やマージはしていないな。マージやるなら、コンフリクトの解消までやりたいよな。どこまでやるかなぁ・・・

あれ？書いたと思った日記がローカルにない。またpushし忘れたか。うーん。
