---
title: "2025年6月24日"
date: 2025-06-24T00:00:00+09:00
lastmod: 2025-06-24T00:00:00+09:00
type: diary
source_month: "d202506.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研システムCにPython3.10.14をインストール。

```sh
curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"
export MAKEOPTS="-j1"
env \
  CFLAGS="-I$HOME/local/libffi/include" \
  LDFLAGS="-L$HOME/local/libffi/lib" \
  PKG_CONFIG_PATH="$HOME/local/libffi/lib/pkgconfig" \
  pyenv install 3.10.14
```

この途中で死ぬ。死んだ上にログインできなくなる。

```sh
$ ssh k011700@kugui1.issp.u-tokyo.ac.jp
shell request failed on channel 0
```

他の端末で監視すると、途中でccが呼ばれなくなっている。インストール中のターミナルでCtrl+Cによりインストールプロセスを殺すとログインできるようになる。なんだこれ？

システムBではどうだろう？

```sh
curl https://pyenv.run | bash
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"
export MAKEOPTS="-j1"
pyenv install 3.10.14
pyenv gloval 3.10.14
```

```sh
$ python3 --version
Python 3.10.14
```

問題なくインストールできた。リソース制限の問題か？

リソース制限の問題だった。

```sh
ulimit -u 300
```

でうまくいった。`make -j 1`を指定しているのに、後ろでプロセスを100個立ち上げている？なぜ？どこで？
