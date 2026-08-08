---
title: "2021年11月15日"
date: 2021-11-15T00:00:00+09:00
lastmod: 2021-11-15T00:00:00+09:00
type: diary
source_month: "d202111.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

いろいろとバタバタして、面接の予定を一個すっぽかしてしまった。申し訳ない。反省。

Macで`latexindent`が動かない。

```txt
$ latexindent
Can't locate YAML/Tiny.pm in @INC (you may need to install the YAML::Tiny module) (@INC contains: /usr/local/texlive/2020/texmf-dist/scripts/latexindent /usr/local/Cellar/perl/5.34.0/lib/perl5/site_perl/5.34.0/darwin-thread-multi-2level /usr/local/Cellar/perl/5.34.0/lib/perl5/site_perl/5.34.0 /usr/local/Cellar/perl/5.34.0/lib/perl5/5.34.0/darwin-thread-multi-2level /usr/local/Cellar/perl/5.34.0/lib/perl5/5.34.0 /usr/local/lib/perl5/site_perl/5.34.0) at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 20.
BEGIN failed--compilation aborted at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/GetYamlSettings.pm line 20.
Compilation failed in require at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/LogFile.pm line 25.
BEGIN failed--compilation aborted at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/LogFile.pm line 25.
Compilation failed in require at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 25.
BEGIN failed--compilation aborted at /usr/local/texlive/2020/texmf-dist/scripts/latexindent/LatexIndent/Document.pm line 25.
Compilation failed in require at /usr/local/bin/latexindent line 27.
BEGIN failed--compilation aborted at /usr/local/bin/latexindent line 27.
```

cpanでYAML::Tinyを入れてやる。

```sh
sudo cpan YAML::Tiny 
```

今度は`File/Homedir.pm`が無い。

```sh
sudo cpan File::HomeDir 
```

これで動くようになった。Macだとlatexindentが自動で走るけど、Windowsでは走らないのなぜだ？

今度はWindowsのWSL2でビルドできない。epstopdfがなかったせいらしい。

```sh
sudo apt-get install texlive-font-utils
```

で入った。

WSL2でlatexindentが走らなかったのはeditor.formatOnSaveがfalseだったかららしい。とにかくこれでフォーマッタが走るようになった。なんかビルド環境を構築するのに一苦労だ。

Subversionの.svnignoreの反映の仕方、毎回ググってる。
