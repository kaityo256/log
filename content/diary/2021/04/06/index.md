---
title: "2021年4月6日"
date: 2021-04-06T00:00:00+09:00
lastmod: 2021-04-06T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

`ffmpeg`が動かない。

```sh
dyld: Library not loaded: /usr/local/opt/aom/lib/libaom.2.dylib
```

またこれか。npmで同じことが起きたときに再インストールでなおったので、再インストールするか。

```sh
$ brew reinstall ffmeg
(snip)
==> python@3.9
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.9

See: https://docs.brew.sh/Homebrew-and-Python
```

なんかPythonが上書きインストールされ、ターミナルからVS Codeが起動しなくなった。

```sh
$ code .
/Users/watanabe/.pyenv/shims/python: line 21: /usr/local/Cellar/pyenv/1.2.23/libexec/pyenv: No such file or directory
/usr/local/bin/code: line 10: ./MacOS/Electron: No such file or directory
```

上記は`pyenv rehash`で治ったが、なんか`Unversioned symlinks`というメッセージがイヤだな。でもいまは忙しいので後回し。

tmuxは便利なんだけど、デフォルトでマウススクロールが使えないのが不便だった。しかし、`~/.tmux.conf`に以下を書くことで解決。

```sh
set -g mouse on
```

しかし、こうすると今度はマウスによる選択ができない。なんとかしようとしてたらtmuxが起動しなくなった。再インストールしてもダメ。結局`/tmp/tmux-501`を削除したら起動できた。

CiscoのWebex Meeting、ログイン時に起動する上に設定がdisabledになっていて修正できなかったので削除した。通常削除もできなかったので、Cisco WebEx Meeting Application Uninstallerなるものをダウンロードしてアンインストール。なんやねん。

tmuxのマウスによる選択、fnキーを押しながらだとできる。これをfn無しにしたい。とりあえずCommand+rでできるようになることはわかったが、.tmux.confで設定する方法がわからない。

なるほど、tmuxが管理するバッファと、ターミナルが管理するバッファが異なるので、マウススクロールでどちらを使うべきかを指示する必要があるのか。マウス処理をどちらに渡すのかを切り替えるのがCommand+rであると。当面はこれで良いか。

いつのまにかGoogleが簡単に英語検索できるようになってた。いや、便利だけど、それでいいのか・・・。
