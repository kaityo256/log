---
title: "2024年4月4日"
date: 2024-04-04T00:00:00+09:00
lastmod: 2024-04-04T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

今日発表の輪講の準備が終わった。直前過ぎる。

自作Pythonパッケージのインストールに失敗。setup.pyに標準パッケージである`logging`を入れたのが原因。無関係の`logging`を入れようとしてバグったらしい。標準パッケージと同じ名前の別のパッケージがあるの、すごく嫌な感じだな。Python2のパッケージがPython3で標準に入ったとか？

ChatGPTに聞いてみた。

> 「PythonのloggingパッケージはPython2から標準パッケージでしたか？」
> PythonのloggingパッケージはPython 2.3で標準ライブラリとして導入されました。これは2003年にリリースされたバージョンです。その前は、loggingモジュールは外部ライブラリとして利用可能でしたが、Pythonの標準ライブラリには含まれていませんでした。したがって、Python 2.3以降、loggingはPythonの標準パッケージとなっています。

なるほど。

シミュレーション工学のページ作った。
