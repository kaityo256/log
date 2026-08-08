---
title: "2026年3月6日"
date: 2026-03-06T00:00:00+09:00
lastmod: 2026-03-06T00:00:00+09:00
type: diary
source_month: "d202603.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

午前中は病院。うーん。

Macにpyenvを入れてみるテスト。

```sh
brew install pyenv
pyenv install 3.11
```

最新のWSL(Ubuntu)にはPython 3.12が入っている。これなら大丈夫かな。

Python3のvenvが入ってなかった。

```sh
sudo apt update
sudo apt install python3.12-venv
```

tensorflowjs_converterを実行したら

```txt
ModuleNotFoundError: No module named 'pkg_resources'
```

というエラーが出る問題、setuptoolsのバージョンが新しすぎるのが原因だったらしい。おそらくuvで入れたときにうまくいかなかったエラーもこれだな。以下のように一度アンインストールし、古いバージョンを指定して入れなおせばOK。

```sh
python3 -m pip uninstall setuptools
python3 -m pip install "setuptools==80.9.0"
```

これ、また一年くらいしたら動かなくなってそうだな・・・
