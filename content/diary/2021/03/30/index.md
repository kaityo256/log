---
title: "2021年3月30日"
date: 2021-03-30T00:00:00+09:00
lastmod: 2021-03-30T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

二年生ガイダンス。

6Fの部屋に机と椅子が入った。あとはPCとか移動するだけか。

Macのlsでファイル名に@がつくやつ、毎回忘れる。これは拡張属性(Extended Attributes, EA)というもので、内容は`ls -l@`で調べることができる。

```sh
$ ls -l@ *.png
-rw-r--r--@ 1 watanabe  staff  134075  3 30 14:21 powershell.png
	com.apple.macl	    72 
-rw-r--r--@ 1 watanabe  staff   43084  3 30 14:26 winver.png
	com.apple.macl	    72 
```

`com.apple.macl`というのがついているらしい。一つ一つ外しても良いが、全部いっきに剥ぎ取る場合は`xattr -c`で良いらしい。`xattr -cr`だとディレクトリを再帰的に潜って消してくれるっぽい。

```sh
$ xattr -c *.png 
$ ls -l@ *.png
-rw-r--r--  1 watanabe  staff  134075  3 30 14:21 powershell.png
-rw-r--r--  1 watanabe  staff   43084  3 30 14:26 winver.png
```

無事に消えた。

WSLのインストールや設定、LammpsのWSL上での実行について書き終わった。
