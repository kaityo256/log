---
title: "2024年1月9日"
date: 2024-01-09T00:00:00+09:00
lastmod: 2024-01-09T00:00:00+09:00
type: diary
source_month: "d202401.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

仕事始め。アナウンスしたりとかメール書いたりとか。

VSCode+ePub環境、絶対あると思って調べてみたらあった。

[VSCode + Markdownでお手軽電子出版](https://qiita.com/ysugimura_it/items/21d1d39b643a0763e6d9)

要点は以下の2つをインストールすること。

* [Markdown Preview Enhanced](https://shd101wyy.github.io/markdown-preview-enhanced/#/)
* [calibre](https://calibre-ebook.com/)

[shd101wyy/ebook-example](https://github.com/shd101wyy/ebook-example)をクローンして、ALICE.mdをプレビューする。そこで右クリックし、「export」「eBook」「ePub」とすると、epubファイルができるはずだが、以下のエラーが出てできない。

```txt
Error: spawn ebook-convert ENOENT
```

調べたら[当該issue](https://github.com/shd101wyy/vscode-markdown-preview-enhanced/issues/1337)を見つけた。

calibreを入れることで入るebook-convertにパスが通っていなかったのが原因(puppeteerは不要っぽい？)。.zshrcに

```sh
export PATH=$PATH:/Applications/calibre.app/Contents/MacOS
```

でコンバートできるようになった・・・が、画像が入らないな。

あと、calibreもスタンドアロン型じゃなくて使いづらいなぁ。単体のePubファイルのビューワーが欲しい。

単体ビューワ、calibreにあった。ebook-viewerだ。こういうのが欲しかった。これで表示すると以下のエラーがでる。

```sh
$ ebook-viewer ALICE.epub
2024-01-09 15:43:21.675 ebook-viewer[70554:3524665] WARNING: Secure coding is not enabled for restorable state! Enable secure coding by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState: and returning YES.
ERROR: clbr://internal.sandbox/book/__index__:0: Not allowed to load local resource: file:///Users/watanabe/github/ebook-example/aiw-illustrations/1book4.jpg
```

要するに外にある画像ファイルをそのまま参照しているため、セキュリティエラーとなっている。

epubはzipファイルだそうなのでunzipして見てみてると、imgタグが絶対パスになっている。

もともとリポジトリに入っていたepubファイルはこんな感じ。

```sh
$ zipinfo -1 ALICE.epub
mimetype
META-INF/
META-INF/container.xml
1book1.jpg
1book2.jpg
1book3.jpg
1book4.jpg
1book5.jpg
1book6.jpg
1book7.jpg
1book8.jpg
1book9.jpg
content.opf
cover.jpg
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_000.html
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_001.html
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_002.html
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_003.html
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_004.html
markdown-preview-enhanced11689-70041-13kc8if.h8bpy3z0k9_split_005.html
page_styles.css
stylesheet.css
titlepage.xhtml
toc.ncx
```

jpgが生でルートに展開されており、htmlがそこを参照するようになっている。ebook-convertはおそらくそこまでやってくれないのｄ，えmarkdown preview enhancedが内部でなにかやっている？

ITCのWS室利用アンケート提出した。

矢上科目の出講希望確定した。

* 物理情報工学ソフトウェア開発演習
    * 昨年のコピー
    * 必要な情報は別途WS室利用アンケートで出しているはず
* 数理物理
    * 昨年のデータがなかった。「ホワイトボードは不可、黒板を希望」「主に板書による講義を実施するため。」で希望を出した。
* シミュレーション工学
    * 昨年のコピー

その他、いっぱいTODOをつぶした。疲れた。
