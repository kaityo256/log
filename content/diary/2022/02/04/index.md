---
title: "2022年2月4日"
date: 2022-02-04T00:00:00+09:00
lastmod: 2022-02-04T00:00:00+09:00
type: diary
source_month: "d202202.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

卒論発表会。いやマジでレベル高い。

予算の締めに走る。

VSCodeがアップデートされ、WSLからcodeを実行しようとしたらこけるようになった。

```sh
$ code .
/mnt/c/Users/watanabe/.vscode/extensions/ms-vscode-remote.remote-wsl-0.63.13/scripts/wslCode.sh: 69: /home/watanabe/.vscode-server-server/bin/5554b12acf27056905806867f251c859323ff7e9/bin/code: not found
```

一度VSCodeをWindowsから起動してリモート接続でWSLにつないで、Serverをダウンロードしたら直った。

FX1000でpbc_testしたが、やはり遅い。それより驚いたのは、Tradモードに対してClangモードが数十倍遅かったこと。原因は乱数。乱数のどこが問題かはまだチェックしていない。

とりあえず[再現ソース](https://gist.github.com/kaityo256/9392bb3984afcdd45d0cb868036788fd)。
