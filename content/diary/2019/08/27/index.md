---
title: "2019年8月27日"
date: 2019-08-27T00:00:00+09:00
lastmod: 2019-08-27T00:00:00+09:00
type: diary
source_month: "d201908.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Macにgem5を入れる。とりあえずclone。

```sh
git clone --depth 1 https://gem5.googlesource.com/public/gem5 
```

ビルドにはsconsが必要なので入れる。

```sh
brew install scons
```

Python2系列じゃないと動かないようだ。

```sh
pyenv local anaconda2-4.4.0
```

```sh
scons build/X86/gem5.opt
```

sconsは、まずbuildを探すが、このディレクトリが存在しないために`build_opts`を探しに行く。するとそこに`X86`があるので、それを参照しつつ、`build`を作って、そこにgem5のバイナリを作る。

ビルドできたらか確認する。

```sh
$ ./build/X86/gem5.opt --version
gem5.opt 2.0
```

できたっぽい。

次、テスト。

```sh
$ ./build/X86/gem5.opt ./configs/example/se.py -c ./tests/test-progs/hello/bin/x86/linux/hello
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Aug 27 2019 12:23:47
gem5 started Aug 27 2019 12:27:22
gem5 executing on watanabe-iMac.local, pid 65602
command line: ./build/X86/gem5.opt ./configs/example/se.py -c ./tests/test-progs/hello/bin/x86/linux/hello

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
Hello world!
Exiting @ tick 5984000 because exiting with last active thread context
```

無事に実行できた。

次、Linuxで作ったバイナリを持ってくる。SEではdynamicリンクができないので、-staticをつける必要がある。

```sh
$ gcc test.c -static
/usr/bin/ld: -lc が見つかりません
collect2: エラー: ld はステータス 1 で終了しました
```

glibcのstaticリンク用ライブラリが必要。

```sh
sudo yum install glibc-static
```

```sh
gcc test.c -static
```

問題なくコンパイルできた。

```sh
./build/X86/gem5.opt ./configs/example/se.py -c a.out
gem5 Simulator System.  http://gem5.org
gem5 is copyrighted software; use the --copyright option for details.

gem5 compiled Aug 27 2019 12:23:47
gem5 started Aug 27 2019 12:35:48
gem5 executing on watanabe-iMac.local, pid 65827
command line: ./build/X86/gem5.opt ./configs/example/se.py -c a.out

Global frequency set at 1000000000000 ticks per second
warn: DRAM device capacity (8192 Mbytes) does not match the address range assigned (512 Mbytes)
0: system.remote_gdb: listening for remote gdb on port 7000
**** REAL SIMULATION ****
info: Entering event queue @ 0.  Starting simulation...
My first md5
Exiting @ tick 6651000 because exiting with last active thread context
Simulated exit code not 0! Exit code is 13
```

実行できたぞ。最後にExit codeについて文句言ってるけど、ちゃんとmain関数の最後で`return 0;`すれば良い。


```sh
./build/X86/gem5.opt --debug-flags=O3PipeView --debug-file=trace.out configs/example/se.py --cpu-type=DerivO3CPU --caches -c ./a.out
```

ただprintfするだけでも7.8 MBのtrace.outが出力される。

```sh
./util/o3-pipeview.py -o pipeview.out --color m5out/trace.out
```

3万2千行(7.5MB)のpipeview.outが出力される。最後に`less -r pipeview.out`すれば見える。
