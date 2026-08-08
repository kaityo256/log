---
title: "2021年8月27日"
date: 2021-08-27T00:00:00+09:00
lastmod: 2021-08-27T00:00:00+09:00
type: diary
source_month: "d202108.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

RevTeX、Ubuntuだと\appendixの動作がおかしい。

WSL2のUbuntuでチェック。まずlatexmkを入れる。

```sh
sudo apt-get update -y
sudo apt-get install -y latexmk
```

RevTeX入ってないな。dkpg -lで調べる。

```sh
dpkg -l | grep texlive
```

texlive-publishersが入ってないな。入れる。

```sh
sudo apt-get install -y texlive-publishers
```

でビルド。あれ？\appendixちゃんと動くなぁ。

GitHub演習の講義ノート続き。いま見たら「Gitはファイルシステムの一種である。ファイルシステムといえばext4である。だからとりあえずinodeについて説明する」とか書いてあって、「それはないな」と正気にかえった。
