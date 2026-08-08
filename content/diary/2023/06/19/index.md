---
title: "2023年6月19日"
date: 2023-06-19T00:00:00+09:00
lastmod: 2023-06-19T00:00:00+09:00
type: diary
source_month: "d202306.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

うお、Macにpptxgrepが入ってない。ビルドしようとしたが、dmdが入ってない。

```sh
git clone git@github.com:kaityo256/pptxgrep.git
cd pptxgrep
brew install dmd
```

コンパイル。

```sh
$ dmd pptxgrep.d
pptxgrep.d(8): Error: unable to read module `xml`
pptxgrep.d(8):        Expected 'std/xml.d' or 'std/xml/package.d' in one of the following import paths:
import path[0] = /usr/local/opt/dmd/include/dlang/dmd
```

うげ。xmlがインポートできない。調べたら`std.xml`が非推奨になってた。もう別の言語で書くか。Rustか、Goかなぁ。面倒だからC++かなぁ。

時間があったらGoで書いてみるか・・・

とりあえずインストールだけ。

* [https://go.dev/dl/](https://go.dev/dl/)に行く
* [https://go.dev/dl/go1.20.5.darwin-amd64.pkg](https://go.dev/dl/go1.20.5.darwin-amd64.pkg)をダウンロード

```sh
$ go version
go version go1.20.5 darwin/amd64
```

はいったぞ。

* VSCodeにRich Go language support for Visual Studio Codeをインストール

そしたらVSCodeがさらに以下のツールを入れた。

```txt
  gotests
  gomodifytags
  impl
  goplay
  dlv
  staticcheck
  gopls
```

後でGoでなんか書いてみよう(←いつだ？)。

数理物理、今回はまともに講義できたけど、反変ベクトル、共変ベクトルの混乱を引きずってるな。来年からは縦ベクトル、横ベクトルとdx, ∂xの双対性だけ説明して、反変、共変の説明はやめよう。
