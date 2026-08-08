---
title: "2018年11月22日"
date: 2018-11-22T00:00:00+09:00
lastmod: 2018-11-22T00:00:00+09:00
type: diary
source_month: "d201811.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数式を含むMarkdownをPDF化しようとして苦労した。
数式がある場合はTeX経由が良いと思われるが、Markdownに外部リソースの画像があると苦しい。というわけでバッジを外した。
あと、Makefileの書き方を真面目に調べたら、もうずいぶん前からサフィックスルールはobsoleteなのね。
というわけでパターンルールで書き直した。
GitHubでもPDFが見えるようになってめでたい。

生のソフトウェアを「バニラ」と呼ぶ語源について。

* IBM's BookMasterでは、デフォルトをvanilla、特別な設定をmochaと呼んでいたらしい。
  * ftp://public.dhe.ibm.com/printers/products/dcf/samples/B2H.HTM
  * https://whatis.techtarget.com/definition/vanilla
* 2005年にLinux KernelのVanillaについて議論がある
  *  http://lkml.iu.edu/hypermail/linux/kernel/0510.1/0248.html

* 1990年に「vanilla workstation」という言い方を見つけた。
  * http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.38.7497&rep=rep1&type=pdf

* 1994年 Vanilla UNIX
  * http://www.ais.org/~jrh/acn/ACN6-1.pdf

* 1989年
  * Vanilla UNIX
  * https://www.usenix.org/legacy/publications/compsystems/1989/fall_shapiro.pdf

* 1985年 COMPUTE! ISSUE 56 / JANUARY 1985 / PAGE 52
  * plain-vanilla BASIC
  * https://www.atarimagazines.com/compute/issue56/107_1_MSX_IS_COMING.php

* 1983年
  * 「vanilla MS-DOS」
  * https://archive.org/stream/byte-magazine-1983-10/1983_10_BYTE_08-10_UNIX_djvu.txt

* 1993年
  * http://www.catb.org/jargon/oldversions/jarg2912.txt

```txt
  THIS IS THE JARGON FILE, VERSION 2.9.12, 10 MAY 1993 
  Applied to hardware and
   software, as in "Vanilla Version 7 UNIX can't run on a
   vanilla 11/34."  Also used to orthogonalize chip nomenclature; for
   instance, a 74V00 means what TI calls a 7400, as distinct from
   a 74LS00, etc. 
```

* 1984年
  * Vanilla UNIX
  * http://www.ittoday.info/AIMS/DSM/84-01-19.pdf

* 1982年のメーリングリスト
  * https://tech-insider.org/vms/research/1982/0111.html

```txt
Date: Tue Jan 19 22:14:54 1982
Subject: VAX/VMS versus Unix
he vanilla version of Unix does not address
these problems, although the Berkeley group has done some work
in this area.
```

* vanilla DOS
  * http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.62.7636&rep=rep1&type=pdf

* 1991
  * http://www.leeandmelindavarian.com/Melinda/neuvm.pdf
  * “Vanilla” CP-67 systems created System/360 virtual machines,

https://archive.org/stream/byte-magazine-1981-09/BYTE_Vol_06-09_1981-09_Artifical_Intelligence_djvu.txt

```txt
BYTE Magazine Volume 06 Number 09 - Artificial Intelligence"
In contrast to the Star, the recently unveiled Xerox 820 
personal computer (see page 441) is disappointing. It's a 
competently designed machine but very "plain vanilla," 
sporting a Z80 processor, CP/M, two 5V4-inch floppy 
disk drives (which give the user a paltry 92 K bytes of 
unformatted storage per floppy disk), and no high- 
resolution graphics.
```

1990年中盤までは「"vanilla"」と二重引用符をつける人が多い。「これは比喩だよ」という意味を込めていると思われる。 

　生JSをVanillaJSと呼ぶ。オリジナルのAngbandもバニラ。
