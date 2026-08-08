---
title: "2025年3月5日"
date: 2025-03-05T00:00:00+09:00
lastmod: 2025-03-05T00:00:00+09:00
type: diary
source_month: "d202503.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WSL2のUbuntuでウェブサイト更新しようとして、そのためにはslimが必要で、そのためにbundlerを使っていて、bundlerが最新のRubyでないと動かず、Rubyのインストールのためにrbenvを入れようとしたら、aptで管理していない、ということなのでgit経由でいれる(なんじゃらほい)。

[Basic Git Checkout](https://github.com/rbenv/rbenv?tab=readme-ov-file#basic-git-checkout)

```sh
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
~/.rbenv/bin/rbenv init 
```

これで`.zprofile`に初期化スクリプトが書き込まれる。シェルを再起動。

```sh
$ rbenv --version
rbenv 1.3.2
```

できた。

```sh
$ rbenv install -l
rbenv: no such command `install'
```

できてない。ruby-buildがないからだそうな。

```sh
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
```

これでできた。

```sh
rbenv install 3.4.2
```

Rubyをソースからビルドしてるのか・・・

```sh
*** Following extensions are not compiled:
psych:
        Could not be configured. It will not be installed.
        Check /tmp/ruby-build.20250305150914.60877.LwvClO/ruby-3.4.2/ext/psych/mkmf.log for more details.

BUILD FAILED (Ubuntu 20.04 on x86_64 using ruby-build 20250215)

You can inspect the build directory at /tmp/ruby-build.20250305150914.60877.LwvClO
```

死んだ。libyaml-devがないのが原因らしい。

```sh
sudo apt update
sudo apt install -y libyaml-dev
rbenv install 3.4.2
```

通った。

```sh
rbenv global 3.4.2
```

これでようやくbundle installが通って、slimが使えるようになった。なんか迂遠すぎる。

タスクを2つ完了。思ったより重かった。なんというか、公開日記に書けない仕事が増えたせいで、日記が日記として役に立ってない。ほぼほぼTodoistのアクティビティログが日記となっている。なんだかなぁ。

英語メールを書いたりした。
