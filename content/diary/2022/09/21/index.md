---
title: "2022年9月21日"
date: 2022-09-21T00:00:00+09:00
lastmod: 2022-09-21T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

iMac復活計画。まずはメール。Thunderbirdを導入。メールはGMailでPOPで読んでいるいるが、GMail+POPは最大30分くらいのタイムラグがあるため、ThunderBird+IMAPでも読めるようにしている。IMAPサーバ上にメールが大量にあったので、少し整理した。

MacにHomebrewをインストール。それに伴い、lab_startupを少し整理。それまでPythonにあったHomebrewのインストールを別ページに独立させた。

ボルツマンマシンの三本目の記事を書き始めた。

リモートにブランチ`branch`がある状態で`git fetch`した。するとローカルに`origin/branch`が出現する。この状態で`git switch branch`とすると、`git switch -c branch origin/branch`と同じことになる。なるほど。これ、どこかにまとめた方が良いかなぁ。
