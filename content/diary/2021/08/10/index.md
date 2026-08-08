---
title: "2021年8月10日"
date: 2021-08-10T00:00:00+09:00
lastmod: 2021-08-10T00:00:00+09:00
type: diary
source_month: "d202108.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Oh、またpush忘れた。プロンプトに表示してあるのに。

Gitでブランチをmasterからmainに変えたときに、

```sh
fatal: ambiguous argument 'origin/main..main': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
```

というエラーが出て困っていたが、これには2つの理由があった。

まず、プロンプトでpush忘れを防ぐために`git log origin/master..master`コマンドが自動で実行されるようになっていた。この状態で、`git branch -m main`として、ローカルのmasterをmainに変えてしまった。upstreamのブランチ名がローカルと違うことを想定していなかったので、`git log origin/main..main`というコマンドが実行されてしまい、そんなパス無いよ、と怒られた。

秋学期の講義の予定をカレンダーに突っ込んだ。やはりHPCI報告会と講義がぶつかるので、事務局に相談。

[Intel C/C++ compilers complete adoption of LLVM](https://software.intel.com/content/www/us/en/develop/blogs/adoption-of-llvm-complete-icx.html) マジか。

なんか、WSL2上にあるファイルをWindows側でいじると、その変更が反映されるのにたまにタイムラグがある気がする。遅延書き込みでもしてるのか？
