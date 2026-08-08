---
title: "2023年9月7日"
date: 2023-09-07T00:00:00+09:00
lastmod: 2023-09-07T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

[理研 AI用スパコン「語岳」整備 「富岳」と組み合わせ「世界一」と同等性能確保](https://ledge.ai/articles/riken_gogaku_fugaku)

ダジャレかい。

bundleを使うたびに使い方をググってる気がする。

```sh
$ bundle -v 
Calling `DidYouMean::SPELL_CHECKERS.merge!(error_name => spell_checker)' has been deprecated. Please call `DidYouMean.correct_error(error_name, spell_checker)' instead.
Bundler version 2.2.24
```

この警告はBundlerが古いから。アップデートすると治る。

```sh
bundle update --bundler
```

ローカルにインストールする時、`--local`はdeprecated. config setで設定していて、installを引数なしで使う。

```sh
bundle config set --local path 'vendor/bundle'
bundle install
```

これ↑も500回くらいググった気がする。

面倒なので`make install`で上記が実行されるようにした。
