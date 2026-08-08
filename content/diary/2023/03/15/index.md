---
title: "2023年3月15日"
date: 2023-03-15T00:00:00+09:00
lastmod: 2023-03-15T00:00:00+09:00
type: diary
source_month: "d202303.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

[Binder比論文が公開されていた](https://doi.org/10.1093/ptep/ptad022)。ついでに自分の業績リストも更新。

K-RISの方はORCID経由で取得できた。Binder比論文はまだ登録されてない。

bundleが「Following files may not be writable, so sudo is needed:」というエラーを出した。

```sh
$ bundle
Using bundler 2.2.24
Using temple 0.8.2
Following files may not be writable, so sudo is needed:
  /opt/rh/rh-ruby27/root/usr/bin
  /opt/rh/rh-ruby27/root/usr/share/gems
  /opt/rh/rh-ruby27/root/usr/share/gems/build_info
  /opt/rh/rh-ruby27/root/usr/share/gems/cache
  /opt/rh/rh-ruby27/root/usr/share/gems/doc
  /opt/rh/rh-ruby27/root/usr/share/gems/extensions
  /opt/rh/rh-ruby27/root/usr/share/gems/gems
  /opt/rh/rh-ruby27/root/usr/share/gems/specifications
```

デフォルトでインストールするgemのパスが変わったらしい。

```sh
$ bundle install --path ~/.gem
[DEPRECATED] The `--path` flag is deprecated because it relies on being remembered across bundler invocations, which bundler will no longer do in future versions. Instead please use `bundle config set --local path '/home/watanabe/.gem'`, and stop using this flag
Could not locate Gemfile
```

ありゃ、書式が古かったらしい。

```sh
export GEM_HOME=$HOME/.gem 
bundle config set --local path ~/.gem
```

これで、Gemfileがあるところでbundle installすればOK。.zshrcに以下を追加しておく。

```sh
export GEM_HOME=$HOME/.gem
export PATH=$PATH:~/.gem/ruby/2.7.0/bin
```

`bundle exec`で実行する場合はPATHの設定は不要。パスにバージョン情報入っちゃってるし、いちいち`bundle exec`経由で実行したほうが良いな。
