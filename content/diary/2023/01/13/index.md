---
title: "2023年1月13日"
date: 2023-01-13T00:00:00+09:00
lastmod: 2023-01-13T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学習指導の仕事にミス。

ポスドクさんの職位申請について失念してた。異動が決まったときにすぐに必要な手続きについて連絡すべきだった。

グループ写真作った。だいぶ大所帯になったなぁ。

いい加減Subversionが面倒になってきた。いま、ファイルを追加してコミットしようとしたら、

```txt
〜.pdfは追加準備状態となっていますが、存在しません
```

というエラーが出る。とりあえず

```sh
svn rm *.pdf
```

してから、ファイル名を英語にして改めて追加したらうまくいった。日本語だったのがまずかった？面倒なので深堀りしないけど。

論文修正しようとしたら、Formatting failed。Macのlatexindentが死んでいるらしい。

```sh
$ latexindent 
Can't locate File/HomeDir.pm in @INC (you may need to install the File::HomeDir module) (@INC contains: /usr/local/texlive/2022/texmf-dist/scripts/latexindent /Library/Perl/5.30/darwin-thread-multi-2level /Library/Perl/5.30 /Network/Library/Perl/5.30/darwin-thread-multi-2level /Network/Library/Perl/5.30 /Library/Perl/Updates/5.30.3 /System/Library/Perl/5.30/darwin-thread-multi-2level /System/Library/Perl/5.30 /System/Library/Perl/Extras/5.30/darwin-thread-multi-2level /System/Library/Perl/Extras/5.30) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 24.
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

いやな感じだなぁ。とりあえず`File::HomeDir`入れてみましょうか。

```sh
sudo perl -MCPAN -e 'install "File::HomeDir"'
```

```sh
$ latexindent 
Please enter text to be indented: (press CTRL+D when finished)
```

あ、うまくいった。なんか時間かかりそうだったけど、あっさりできてよかった。

いやしかし、何を書いても文句を言う人がいる、という感じだなぁ……

うーん、例えばさ、初めてPIとなる人が、自分の研究室をどのように運営するかって悩むじゃない？もちろん自分の出身研究室は大いに参考になるけど、時代も変わってくわけだし。その時に、他の研究室がどう運営しているかを公開してくれてたら助かるじゃない。例えば研究室の連絡にLineやSlackを使ってるという話を聞くとして、具体的にどういう使い方をしているかって気になるじゃない。特にSlackみたいな自由度が高いツール、どう使えばよいかはわからないよね。

そういう時に、ある程度使ってみて「こういう風に運営してうまくいっているよ」という事例があると、すごく助かると思うんだよね。その事例を見て、参考になるところは参考にすれば良いし、違うなと思えば変えれば良いし。

いずれにせよ、僕には情報を公開するメリットは無いんだ。でも公開するのは、そうやって他の人が公開してくれた情報で助かったことがあり、「次は僕の番」って思ってるからなんですよ。
