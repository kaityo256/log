---
title: "2023年1月8日"
date: 2023-01-08T00:00:00+09:00
lastmod: 2023-01-08T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

がんばれなかった。

[一週間でなれる！スパコンプログラマ](https://github.com/kaityo256/sevendayshpc)にissue。図にリンクミスがあり、このリンクミスはMarkdown、HTMLともに修正済みだが、PDFが修正されていないので修正して欲しいとのこと。

で、Releaseを見てみたら、ちゃんと修正されている。アレ？と思って見てみたら、「PDF版はこちら」と、リポジトリのファイルに直リンしており、それが古い。つまり、

* 僕がMarkdownを修正した後
* HTMLを作成し、
* PDFをビルドし、
* Releaseを作成して、そのAssetsにPDFを追加するところ

までは忘れなかったが、

* 作成したPDFをリポジトリのトップ階層にコピーしてcommit & push

することは忘れていたということか。

「PDF版はこちら」で、リリースの方をリンクするのが良いのだろうか。一応`releases/latest`で最新リリースにリンクできるが、それだと、PDFのダウンロードに二回クリックが必要になってしまう。

・・・と思っていたが、今は

```txt
https://github.com/USER/PROJECT/releases/latest/download/package.zip
```

が、最新リリースの`package`にリダイレクトされるようになったらしい。

→[Is there a link to GitHub for downloading a file in the latest release of a repository?](https://stackoverflow.com/a/54836319)

つまり、リリースにPDFを含めることを忘れなければ、常に、

```txt
https://github.com/kaityo256/sevendayshpc/releases/latest/download/sevendayshpc.pdf
```

というリンクが最新のPDFを指すようになった。うん、リポジトリ直よりこっちの方が良いな。
