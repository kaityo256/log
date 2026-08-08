---
title: "2019年2月21日"
date: 2019-02-21T00:00:00+09:00
lastmod: 2019-02-21T00:00:00+09:00
type: diary
source_month: "d201902.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

明日のセミナーの準備。あと、たまっていた書類仕事とか。

WSLにD言語をインストール。

```sh
mkdir build
cd build
wget http://downloads.dlang.org/releases/2.x/2.084.1/dmd_2.084.1-0_amd64.deb
sudo apt install ./dmd_2.084.1-0_amd64.deb
```

WindowsにD言語をインストールした。

VSCodeにcode-dをインストールしたが、dfmtはインストールされなかったようだ。
dfmtを入れるのに、gitがいるっぽい。なので、[ここ](https://git-scm.com/download/win)からWindows用のgitを入れた。
