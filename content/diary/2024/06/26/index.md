---
title: "2024年6月26日"
date: 2024-06-26T00:00:00+09:00
lastmod: 2024-06-26T00:00:00+09:00
type: diary
source_month: "d202406.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Jekyllを試す。まずはJekyllをインストール。

```sh
gem install jekyll
mkdir jekyll_test 
cd jekyll_test
bundle init
```

GemfileにJekyllを追加。

```sh
bundle config set path 'vendor/bundle'
bundle install
bundle exec jekyll s
```

```sh
bundle exec jekyll new . --force
bundle install
```

駄目だ。よくわからん。もっと簡単なやつが欲しい。

hugoを試す。

```sh
brew install hugo
hugo new site hugo_test
cd hugo_test
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml
hugo server
```

できた。

んー、でもよくわかんないや。もう面倒だからPandocで行く。すまん。

結局Markdown+Pandocで書いた。うーむむ。
