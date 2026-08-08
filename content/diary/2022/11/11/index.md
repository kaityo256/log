---
title: "2022年11月11日"
date: 2022-11-11T00:00:00+09:00
lastmod: 2022-11-11T00:00:00+09:00
type: diary
source_month: "d202211.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

なんか疲れた。忙しかったし、一週間日記を書く余裕もなかった。金曜日に一週間分振り返って書いている。

学生さんの論文チェック。これで投稿できるかな。その前に英文校閲出す。

しまった、会議の時間が変わってて、別のミーティングとぶつかってしまった。

GitHub演習、無事に終わった。全員BANされてなかった。GitHubから「直しておく」という連絡が来ていたが、ちゃんとやっておいてくれたらしい。良かった。GitHub Supportのチケットを閉じておく。

とにかく今年もGitHub演習が終わった。二回やってみて、学生が詰まるところがわかってきた気がするので、忘れないうちに修正してしまおう。来年あたりはかなりスムーズに行くはず？

Macをupdateしたらmakeが使えなくなった。

```sh
$ make
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
```

例によってXcodeがらみらしい。

```sh
xcode-select --install
```

でインストール。なんか残り30分とか出るんだけど・・・

なんか5分で終わった。make使えるようになった。
