---
title: "2025年8月26日"
date: 2025-08-26T00:00:00+09:00
lastmod: 2025-08-26T00:00:00+09:00
type: diary
source_month: "d202508.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ずっと目がかゆいし赤い。アレルギーではなく、アデノウイルスだっただろうか？

MacにJuliaをインストール。

```sh
brew update
brew upgrade
brew install julia
```

しようかと思ったが、upgradeに時間がかかりすぎてる。次。

また、TeXのformattingに失敗。

```sh
$ latexindent manuscript.tex
Can't locate YAML/Tiny.pm in @INC (you may need to install the YAML::Tiny module) (@INC entries checked: /usr/local/texlive/2025/texmf-dist/scripts/latexindent /usr/local/opt/perl/lib/perl5/site_perl/5.40/darwin-thread-multi-2level /usr/local/opt/perl/lib/perl5/site_perl/5.40 /usr/local/opt/perl/lib/perl5/5.40/darwin-thread-multi-2level /usr/local/opt/perl/lib/perl5/5.40 /usr/local/lib/perl5/site_perl/5.40/darwin-thread-multi-2level /usr/local/lib/perl5/site_perl/5.40) at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/UTF8CmdLineArgsFileOperation.pm line 107.
BEGIN failed--compilation aborted at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/UTF8CmdLineArgsFileOperation.pm line 107.
Compilation failed in require at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/LogFile.pm line 34.
BEGIN failed--compilation aborted at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/LogFile.pm line 34.
Compilation failed in require at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 29.
BEGIN failed--compilation aborted at /usr/local/texlive/2025/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 29.
Compilation failed in require at /usr/local/bin/latexindent line 28.
BEGIN failed--compilation aborted at /usr/local/bin/latexindent line 28.
```

```sh
$ brew install perl
Warning: perl 5.40.2 is already installed and up-to-date.
To reinstall 5.40.2, run:
  brew reinstall perl

$ brew install cpanminus
Warning: cpanminus 1.7048 is already installed and up-to-date.
To reinstall 1.7048, run:
  brew reinstall cpanminus
```

両方入ってるな。

```sh
cpanm YAML::Tiny File::HomeDir File::Find::Rule Unicode::GCString
```

なんかVSCodeのLaTeXがDockerを要求するようになった。

```json
    "latex-workshop.docker.enabled": true,
```

なんだこりゃ？Docker関連の拡張機能を全て削除。Docker DXとDocker、Dev Containersが入ってた。その上で、

```json
    "latex-workshop.docker.enabled": false,
```

にしたらうまくいった。

あと、Formatterがうまく動かなかった件も解決。こちらはPerlの問題っぽいな。

なんか本質的ではないところで疲弊する・・・

論文のイントロまで完成。あとは細かいところのチェック。
