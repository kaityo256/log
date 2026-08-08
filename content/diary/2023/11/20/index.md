---
title: "2023年11月20日"
date: 2023-11-20T00:00:00+09:00
lastmod: 2023-11-20T00:00:00+09:00
type: diary
source_month: "d202311.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

textlintを入れようとしたがnode.jsが古かったっぽい。

```sh
brew install nodebrew 
```

`.zshrc_mine.zsh`に以下を追加。

```sh
export PATH=$HOME/.nodebrew/current/bin:$PATH
```

最新版をインストール。

```sh
nodebrew install latest
```

```sh
$ nodebrew list  
v21.2.0

current: none
```

バージョン指定。

```sh
nodebrew use @v21.2.0
```

うまくいかない。

あー、nvmもインストールしてて、それとぶつかってた。

```sh
nvm install 20.9.0
nvm use v20.9.0
```

以下は執筆ディレクトリで。

```sh
npm init -y
npx textlint --init
npm install --save-dev \
    textlint \
    textlint-rule-preset-ja-spacing \
    textlint-rule-preset-ja-technical-writing \
    textlint-rule-spellcheck-tech-word
```

いまいち`packages.json`がよくわかっていない。一度これを作ったら、あとは

```sh
npm install
```

でどこも同じ環境になる、という理解でいいのか？bundleも同じ？
