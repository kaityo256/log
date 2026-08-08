---
title: "2025年1月9日"
date: 2025-01-09T00:00:00+09:00
lastmod: 2025-01-09T00:00:00+09:00
type: diary
source_month: "d202501.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

今度は水曜日の分をpushし忘れた。やれやれだ。

指導委託延長書類返した。

VSCodeのLaTeX フォーマッタがエラー。

```txt
Formatting failed. Please refer to LaTeX Workshop Output for details.
```

```sh
$ latexindent -l manuscript.tex
Attempt to call undefined import method with arguments ("@logFileLines") via package "LatexIndent::Logger" (Perhaps you forgot to load the package?) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 28.
Can't locate YAML/Tiny.pm in @INC (you may need to install the YAML::Tiny module) (@INC entries checked: /usr/local/texlive/2022/texmf-dist/scripts/latexindent /usr/local/opt/perl/lib/perl5/site_perl/5.40/darwin-thread-multi-2level /usr/local/opt/perl/lib/perl5/site_perl/5.40 /usr/local/opt/perl/lib/perl5/5.40/darwin-thread-multi-2level /usr/local/opt/perl/lib/perl5/5.40 /usr/local/lib/perl5/site_perl/5.40) at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 22.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 22.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Verbatim.pm line 23.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Verbatim.pm line 23.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Lines.pm line 23.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Lines.pm line 23.
Compilation failed in require at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 30.
BEGIN failed--compilation aborted at /usr/local/texlive/2022/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 30.
Compilation failed in require at /usr/local/bin/latexindent line 27.
BEGIN failed--compilation aborted at /usr/local/bin/latexindent line 27.
```

TeXLiveが古いな。

```sh
$ tlmgr --version  
tlmgr revision 63068 (2022-04-18 07:58:07 +0200)
tlmgr using installation: /usr/local/texlive/2022
TeX Live (https://tug.org/texlive) version 2022
```

だめだ。後で新しいのをインストールしないと。

ガイダンス。

研究室ミーティング。自己紹介。

お仕事いっぱい。

超久しぶりにコーディング。だいぶなまっている。
