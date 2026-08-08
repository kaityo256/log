---
title: "2021年5月27日"
date: 2021-05-27T00:00:00+09:00
lastmod: 2021-05-27T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

多分火曜日と水曜日の日記書いたけど、家に置いてきた。も〜。

昨日、ついかっとなって[三角関数の話](https://zenn.dev/kaityo256/articles/trigonometric_function)を書いてしまった。そんな暇全然無いんだけど。なんというか、三角関数不要論に限らないけど、世の中を「わかってる人」「わかってない人」にわけて、自分が「わかってる人」に分類されることを確認して安心する、というプロセス、やりたくなる気持ちはわからないではないけど、なんにも生み出さないよ。

ParaViewのハンズオン、動作確認。Pythonまわりの記述が古かったのを修正。

ParaViewを研究室サーバにインストール。`ParaView-5.9.1-MPI-Linux-Python3.8-64bit.tar.gz`をダウンロード。

```sh
cd build
tar xvzf ParaView-5.9.1-MPI-Linux-Python3.8-64bit.tar.gz
cd ParaView-5.9.1-MPI-Linux-Python3.8-64bit
cd bin
./paraview
```

```sh
$ ./paraview
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
(   9.209s) [paraview        ]vtkOpenGLRenderWindow.c:471    ERR| vtkXOpenGLRenderWindow (0x14de0490): Unable to find a valid OpenGL 3.2 or later implementation. Please update your video card driver to the latest version. If you are using Mesa please make sure you have version 11.2 or later and make sure your driver in Mesa supports OpenGL 3.2 such as llvmpipe or openswr. If you are on windows and using Microsoft remote desktop note that it only supports OpenGL 3.2 with nvidia quadro cards. You can use other remoting software such as nomachine to avoid this issue.
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
(  10.143s) [paraview        ]vtkOpenGLRenderWindow.c:471    ERR| vtkXOpenGLRenderWindow (0x15f6c120): Unable to find a valid OpenGL 3.2 or later implementation. Please update your video card driver to the latest version. If you are using Mesa please make sure you have version 11.2 or later and make sure your driver in Mesa supports OpenGL 3.2 such as llvmpipe or openswr. If you are on windows and using Microsoft remote desktop note that it only supports OpenGL 3.2 with nvidia quadro cards. You can use other remoting software such as nomachine to avoid this issue.

Loguru caught a signal: SIGSEGV
```

SIGSEGVで死んだ。MacのOpenGLのせいかと思ってWSLから接続してもダメ。諦めた方が良いかな？

一応試すか。Qtをインストール・・・しようとしたらログインを要求された。なんかも〜。

M1 Macに普通に入ったっぽいので、DockerやLinuxインストールはやめ。普通にハンズオンできた。良かった。
