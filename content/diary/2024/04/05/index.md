---
title: "2024年4月5日"
date: 2024-04-05T00:00:00+09:00
lastmod: 2024-04-05T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

サイトに卒業式、学位授与式の情報を追加。ついでにウェブサイトのCocoonの設定をいろいろ変更。

懸案だった「過去のお知らせ一覧」を表示できるようにした。まず、URLとしては`https://www.calc.appi.keio.ac.jp/category/news/`でお知らせ一覧が表示できる。これをサイドバーにいれる。

方法はCocoon設定ではなく「外観」「カスタマイズ」「ウィジェット」「サイドバー」。そこに

```txt
[showwhatsnew]
```

とあるのを、

```txt
[showwhatsnew]
もっと見る
```

にして、「もっと見る」から[https://www.calc.appi.keio.ac.jp/category/news/](https://www.calc.appi.keio.ac.jp/category/news/)にリンクをはった。

latexindentが動かない。

```sh
$ latexindent
Can't locate File/HomeDir.pm in @INC (you may need to install the File::HomeDir module) (@INC contains: /usr/local/texlive/2022/texmf-dist/scripts/latexindent /Library/Perl/5.34/darwin-thread-multi-2level /Library/Perl/5.34 /Network/Library/Perl/5.34/darwin-thread-multi-2level /Network/Library/Perl/5.34 /Library/Perl/Updates/5.34.1 /System/Library/Perl/5.34/darwin-thread-multi-2level /System/Library/Perl/5.34 /System/Library/Perl/Extras/5.34/darwin-thread-multi-2level /System/Library/Perl/Extras/5.34) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 24.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 24.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Verbatim.pm line 23.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Verbatim.pm line 23.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Lines.pm line 23.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Lines.pm line 23.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 30.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 30.
Compilation failed in require at /usr/local/bin/latexindent line 27.
BEGIN failed--compilation aborted at /usr/local/bin/latexindent line 27.
```

[ここ](https://zenn.dev/ganariya/articles/vscode-latex-indent)を参考に設定してみる。

```sh
brew install perl
brew install cpanm
cpanm Log::Log4perl Log::Dispatch::File YAML::Tiny File::HomeDir Unicode::GCString
```

latexindentがエラーを出さなくなった。VSCodeもlatexindentがそのまま通るようになった。

春季安全教育提出した。

就任なんとか計画出した。

今日はタスク9個終わらせたが2個終わらなかった。
