---
title: "2023年6月29日"
date: 2023-06-29T00:00:00+09:00
lastmod: 2023-06-29T00:00:00+09:00
type: diary
source_month: "d202306.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

yaml_cvにPR。Ruby 3.1以降で動かないらしい。確認。まずMacにRuby 3.1をインストールするためにrenvを入れる。

```sh
brew install rbenv ruby-build
```

```sh
$ rbenv init - 
export PATH="/Users/watanabe/.rbenv/shims:${PATH}"
export RBENV_SHELL=zsh
source '/usr/local/Cellar/rbenv/1.2.0/libexec/../completions/rbenv.zsh'
command rbenv rehash 2>/dev/null
rbenv() {
  local command
  command="${1:-}"
  if [ "$#" -gt 0 ]; then
    shift
  fi

  case "$command" in
  rehash|shell)
    eval "$(rbenv "sh-$command" "$@")";;
  *)
    command rbenv "$command" "$@";;
  esac
}
```

出てきた内容を`.zshrc`に追加(僕の場合は`.zshrc_mine.zsh`)。

```sh
$ rbenv install --list
3.0.6
3.1.4
3.2.2
jruby-9.4.3.0
mruby-3.2.0
picoruby-3.0.0
truffleruby-23.0.0
truffleruby+graalvm-23.0.0

Only latest stable releases for each Ruby implementation are shown.
Use 'rbenv install --list-all / -L' to show all local versions.
```

まず2.6で実行。

```sh
$ ruby --version
ruby 2.6.10p210 (2022-04-12 revision 67958) [universal.x86_64-darwin22]
$ ruby make_cv.rb
input  file: data.yaml
style  file: style.txt
output file: output.pdf
Done.
```

できてる。

```sh
$ rbenv install 3.2.2
$ rbenv global 3.2.2  
$ ruby --version
ruby 3.2.2 (2023-03-30 revision e51014f9c0) [x86_64-darwin22]
```

いつのまにか、Rubyで`Dir.exists?`と`File.exists?`が非推奨になったと。

というわけでPRをマージしたらRuby 3.2.2でも動くことを確認。さらに、bundle --without documentationがdeprecatedになっていたので、

```sh
bundle config path vendor/bundle
bundle config set --local without 'documentation'
bundle install
```

と、ローカル設定するよう修正。

さらに、前からやろうやろうと思っていたIPAフォントの同封を実施。ライセンスをちゃんと読んだら同封して良さそうだったので。こういうオリジナルライセンスって、きっちり読まないと何をして良いか、よくないかがわからないので面倒なんだよなぁ。

しかし、しばらく触ってないといろんなものがdeprecatedになってて、それで世の中の進歩を知る感じになって、自分だけ取り残されてる気持ちになってイヤになりますね。

古いバージョンのRubyを入れる。

```sh
rbenv install 2.7.8  
rbenv local 2.7.8
```

うん、どちらも動くようになった。

結局、PrawnのGemがメンテされていないのが悪いので、

```sh
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "prawn", github: "prawnpdf/prawn"
```

と、GitHubから取るようにすればOKだった。これで`matrix`は不要。

ついでに前から気になってた[lammps_collision](https://github.com/kaityo256/lammps_collision)の`format`文字列をf-stringに修正。学生さんがこれをスタートに改造することが多いので、formatを使い続けちゃうんだよね。
