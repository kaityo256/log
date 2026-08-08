---
title: "2021年3月24日"
date: 2021-03-24T00:00:00+09:00
lastmod: 2021-03-24T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

VS CodeのMarkdown Preview、いつのまにか画像が更新された時にプレビューが自動で更新されるようになってる。便利。

gnuplotハンズオンの準備できた。

論文修正しようとしたら、家での修正をpushし忘れてた orz

大幅な修正だったのでマージせずに作業するのは不可能。うーむ。

VSCodeのrubocopが死んでいる。ターミナルで実行してみたら

```txt
$ rubocop
/usr/local/Cellar/ruby/3.0.0_1/lib/ruby/3.0.0/rubygems.rb:281:in `find_spec_for_exe': can't find gem rubocop (>= 0.a) with executable rubocop (Gem::GemNotFoundException)
  from /usr/local/Cellar/ruby/3.0.0_1/lib/ruby/3.0.0/rubygems.rb:300:in `activate_bin_path'
  from /usr/local/bin/rubocop:22:in `<main>'
```

とのこと。gemで入れ直したら治った。

```sh
gem install rubocop 
```

論文のデータ整理。いろいろ悩ましい。

arXiv死んでる？それとも大学からのアクセスが拒否られている？

復活した。なんだったんだろう。
