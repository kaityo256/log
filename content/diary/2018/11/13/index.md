---
title: "2018年11月13日"
date: 2018-11-13T00:00:00+09:00
lastmod: 2018-11-13T00:00:00+09:00
type: diary
source_month: "d201811.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

MDACPの開発をGitHubに一本化する。これまで自前サーバでSubversion、
自前サーバでgit-svn、そして自前サーバでgitとVCSを変えてきたのだが、要望があってGitHubにリポジトリを上げた。
そうしたらどれが最新かよくわからなくなってきたので。今日、DiffをとってGitHub版が最新であることを確認。
ローカルのリポジトリを消した。

　ついでにSourceForge.netのウェブサイトもObsoleteにした。SourceForge.netでは、
/home/project-web/mdacp/htdocsがウェブ置き場になっている。ここを書き換える。

　で、Kで開発環境を整えようと.vimrcをコピーしたらエラー。Vimのバージョンが古い。しょうがないので8.0を入れる。
<a href="d201805.html#d04">この手順</a>でいけた。昔の俺GJ。

　Kでmakefile.dependを作れるようにmakefileを修正。

　午前中はSF.netからGitHubへのリダイレクトとKの開発環境構築で溶けた。

　Mac Mojaveではgdbが使えない。原因は<a href="https://stackoverflow.com/questions/52529838/gdb-8-2-cant-recognized-executable-file-on-macos-mojave-10-14">ここ</a>にあるように、新しいロードコマンドを追加したから。

```sh
$ git clone --depth 1 git://sourceware.org/git/binutils-gdb.git  
$ ./configure
$ make
In file included from ./../include/alloca-conf.h:16,
                 from xsym.c:24:
./../intl/config.h:210: error: "PACKAGE_VERSION" redefined [-Werror]
 #define PACKAGE_VERSION ""
 
In file included from sysdep.h:29,
                 from xsym.c:23:
config.h:325: note: this is the location of the previous definition
 #define PACKAGE_VERSION "2.31.51"
 
cc1: all warnings being treated as errors
make[4]: *** [xsym.lo] Error 1
make[3]: *** [all-recursive] Error 1
make[2]: *** [all] Error 2
make[1]: *** [all-bfd] Error 2
make: *** [all] Error 2
```


　うーん、コケますね。
