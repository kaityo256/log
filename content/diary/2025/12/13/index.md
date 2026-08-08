---
title: "2025年12月13日"
date: 2025-12-13T00:00:00+09:00
lastmod: 2025-12-13T00:00:00+09:00
type: diary
source_month: "d202512.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

長い会議。

家のPCのセットアップ。

1. WSLをインストール
1. gitでdotfilesをクローンして設定
1. keychainの設定
1. 公開鍵の登録(GitHub、ウェブサーバ、計算サーバ)
1. Subversionで研究用のリポジトリ落とす

論文やコードはGit管理してるんだけど、セミナー用のスライドや日々の会議、授業管理などはすべてSubversion管理している。で、仕事用リポジトリとセミナー用リポジトリにすべてまとめているので、それらを落とせば研究環境構築完了。やっぱり便利だ。

```sh
svnserve: warning: cannot set LC_CTYPE locale
svnserve: warning: environment variable LANG is C.UTF-8
svnserve: warning: please check that your locale name is correct
```

これはサーバ側にC.UTF-8やja_JP.utf8がないから。サーバのOSをアップデートしないとダメだな・・・

`.bashrc`に

```sh
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
alias dc='cd'
alias ls='ls --show-control-char -F --color'

bind '"\C-n": history-search-forward' 2>/dev/null
bind '"\C-p": history-search-backward' 2>/dev/null
HISTSIZE=100000
```

を書かせるようにしたほうが良いな。
