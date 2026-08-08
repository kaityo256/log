---
title: "2024年3月19日"
date: 2024-03-19T00:00:00+09:00
lastmod: 2024-03-19T00:00:00+09:00
type: diary
source_month: "d202403.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

土曜日のignite sessionのスライド作って送った。

GitHubに公開されているPythonパッケージをGoogle Colabにインストールする方法。

リポジトリがパブリックな場合はpipでそのままインストールできる。

```py
!pip3 install git+https://github.com/kaityo256/package_sample.git
```

プライベートな場合はPersonal Access Tokenが必要。しかし、これを使うと「全ての」リポジトリにアクセスできてしまう。

そこで、GitHubのプライベートリポジトリとして公開されているPythonライブラリをDeploy Keysを使ってpipでインストールしようとしたが、うまくssh-agentにつながらない。ちょっと無理っぽいなぁ。
