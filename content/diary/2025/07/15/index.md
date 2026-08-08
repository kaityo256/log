---
title: "2025年7月15日"
date: 2025-07-15T00:00:00+09:00
lastmod: 2025-07-15T00:00:00+09:00
type: diary
source_month: "d202507.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Rubyのパッケージ管理、まだ良くわかってない。

```sh
bundle config set --local path 'vendor/bundle'
```

を実行すると、`.bundle/config`というファイルが作成される。中身は

```ruby
---
BUNDLE_PATH: "vendor/bundle"
```

これがあると、

```sh
bundle install
```

とだけした場合でも、ローカルにインストールしてくれる。`source .venv/bin/activate`が不要なのは良さげ。

`bundle install`を実行すると、そこにある`Gemfile`を参照する。今回はHexaPDFを使いたいので以下のように記述する。

```ruby
# Gemfile
source "https://rubygems.org"

gem "hexapdf", "~> 1.3"
```

`.gitignore`には、`vendor`は追加するが、`.bundle`は入れない、すなわち`.bundle`はリポジトリ管理する。

HexaPDFをインストールしようとしたら、

```sh
An error occurred while installing openssl (3.3.0), and Bundler cannot continue.

In Gemfile:
  hexapdf was resolved to 1.3.0, which depends on
    openssl
```

なんでPDF解析ライブラリがopensslに依存しているんだ？

```sh
sudo apt-get install libssl-dev 
```

このあと、

```sh
bundle install
```

したらうまくいった。

なんか昔の論文に質問が来たので答えた。

数理物理の講義後半予想問題集および解答例を作ってアップロードし、期末試験の案内流した。

前から作ろうと思ってた奴、ようやくできた。

[Font Size Analyzer for PDF Documents](https://github.com/kaityo256/pdf-fontsize-analyzer)

明らかにLaTeXから出力したPDFの方がフォントサイズが小さい。なぜだ？あと、Mac Wordから作ったPDFはカウントできない。
