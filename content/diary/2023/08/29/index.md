---
title: "2023年8月29日"
date: 2023-08-29T00:00:00+09:00
lastmod: 2023-08-29T00:00:00+09:00
type: diary
source_month: "d202308.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学生さん論文の査読レポート返ってきた。比較的好意的なレポート。良かった。適切に返事をすれば通るだろう。

前から縦書きの本を書きたいと思っていた。重い腰を上げてRe:VIEWでやってみることに。今は横書きの本をRe:VIEW starterで書いているが、生Re:VIEWも扱ってみる。

まずはRe:VIEWのインストール。

```sh
sudo gem install review
```

gemをアップデートしろと言われた。

```sh
sudo gem update --system
sudo gem update
```

`--system`がgem自体のアップデート、なしだとインストールされている各gemのアップデート。

```sh
$ which review
/Users/watanabe/.rbenv/shims/review
```

全く忘れていたが、rbenvで管理しているんだな。

サンプルプロジェクトを作成してビルド。

```sh
cd github
review-init rvsample
cd rvsample
review-epubmaker config.yml
```

book.epubができるので、

```sh
open book.epub
```

すると、iBookで開く。ここまでOK。

縦書きは、[ここ](https://github.com/kmuto/review/blob/master/doc/writing_vertical.ja.md)に従う。

そのままだと「第1章」の1だけ横向きになるので、例えば`local.yml`に

```yaml
locale: ja
chapter: "第%pJ部"
```

みたいに書くと第一部と漢数字になる。

iBookはデバッグに全く向かない。開く度に本棚に登録されてしまう。なんかちょうどよいepub Readerはないかな。

開きっぱなしで、ファイルが更新された再読み込みされるものが良い。

ChromeにはReadiumというものがあったが、[GoogleがChrome Appsのサポートをやめたらしい](https://blog.chromium.org/2020/01/moving-forward-from-chrome-apps.html)。アナウンスを読んでも、なぜAppsをやめたかよくわからない。

拡張機能は継続と。[Chromeアプリ版として別途開発、サポートするのが大変だから、これからはAndroidアプリ版やWebアプリ版、Webサービスを使ってね](https://office-kabu.jp/chromebook/miscellaneous-impressions/chromebook-20200117)ということらしい。

Readiumは拡張機能ではなく、Chrome Appsとして開発されていたため、この決断により使えなくなったと。

Chromeのepub Reader使ってみたけど、表示が崩れてどうにもならなかった。iBookでなんとかするしかないのか？PDFで中身だけ確認して、偶に縦書きをEPUBで確認、みたいな。
