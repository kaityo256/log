---
title: "2019年6月11日"
date: 2019-06-11T00:00:00+09:00
lastmod: 2019-06-11T00:00:00+09:00
type: diary
source_month: "d201906.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Formuraを入れてみる。[ここ](https://qiita.com/hrontan/items/ae8b3d5f8e999525f4b9)を参考に。
まずはhaskellのインストール。

```sh
brew install haskell-stack
git clone git@github.com:nushio3/formura.git
```

```sh
git clone git@github.com:nushio3/formura.git 
cd formura
stack setup --install-ghc
stack build --trace
```

初回実行は結構時間がかかる。と思ったら上記は古かった。あたらしいリポジトリは[ここ](https://github.com/formura/formura)だ。

```sh
git clone git@github.com:formura/formura.git
cd formura
stack install
```

あとはsampleとかで遊べる。
