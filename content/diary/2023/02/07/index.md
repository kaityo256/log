---
title: "2023年2月7日"
date: 2023-02-07T00:00:00+09:00
lastmod: 2023-02-07T00:00:00+09:00
type: diary
source_month: "d202302.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

gitでsubmoduleがおかしくなり、git pullとかしようとしても

```sh
fatal: no submodule mapping found in .gitmodules for path 'submodule'
```

とか言われてしまうようになった。Gitとしてはsubmobuleがあると認識しているのに、`.gitsubmodule`もないし、`.git/config`にも情報がない。

これを直すには、まずファイルパーミッションがSubmoduleになっているものを探す。

```sh
$ git ls-files --stage | grep 160000
160000 71de7d435da4887140e445a5caf1cdf0e1a3119b 0 submodule
```

これを削除する。

```sh
git rm --cached submodule
```

これで後はコミットすればOK。

VSCode上でdiffを見ようと思ってGit Lensを導入……したが、使い方がよくわからなかった。以前もインストールしたような気がしたが、と思ったが、これ、Git管理されているファイルの変更されたすべての行にいちいちアノテーションがつくのが鬱陶しくてやめたんだ。とりあえずアンインストール。

研究室Wiki(Pukiwikiで運用)が使いづらくて仕方ないので、GitHubのプライベートリポジトリへ移行する。とりあえずリポジトリを作って、2020年度の卒論だけ追加しておいた。

Gitの日本語diff、なかなかうまくいかなかったんだけど、多分これでできた。

```sh
git diff --word-diff-regex=. main thesis.tex
```

プログラミング基礎同演習、採点確定した。

修士論文発表会の準備した。発表セットに会場案内図、プログラムを印刷して配る。今回からレーザーポインタとType-Cコネクタが追加。

特異値分解論文のProof返した。
