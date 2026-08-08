---
title: "2021年4月14日"
date: 2021-04-14T00:00:00+09:00
lastmod: 2021-04-14T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

SNSで科研費に落ちたと思しき人の呪詛を見てしまった。「自分の科研費が落ちたのは審査員がわかっていないせいだ」と思っていると、たぶん次も落ちる可能性が高いと思う。そもそも分野が近い人が審査しているのだから、そういうことを言うのはやめたほうが良い。

その、そもそも論として「論文の査読」「科研費の審査」「人事公募」といった「評価」にまつわるもの、「向こう側に自分と同じ人間がいる」という認識を持たないといろいろ危ういと思う。文句を言う人は、なんか国とかそういう「権力」に近い、非人間的な何かを想像しているのではないか？

MacでOpenGLが走らない。ssh越しでもダメ。そもそもOpenGLがdeprecatedになっているらしくて、X越しでもVMDが動かなくて困る。

で、うっかりサーバで`yum update`したら更新パッケージ1460個とか。うげー。

面倒だから別の端末で`sudo yum install glx-utils.x86_64`したら、

```txt
ロックファイル /var/run/yum.pid が存在します: PID 213375 として別に実行されています。
```

と怒られた。ですよね。

CentOSにffmpegを入れる。

```sh
sudo yum -y install epel-release
sudo yum -y localinstall --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
sudo yum -y install ffmpeg ffmpeg-devel
```

Mac経由でCentOSにつないだらglxfinfoが動かない。

```sh
$ glxinfo
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
X Error of failed request:  GLXBadContext
  Major opcode of failed request:  149 (GLX)
  Minor opcode of failed request:  6 (X_GLXIsDirect)
  Serial number of failed request:  31
  Current serial number in output stream:  30
```

libGL errorはWindowsでも出る。問題はその後の`GLXBadContext`だな。

Macのパラメタを見てみる。

```sh
$ defaults read org.xquartz.X11
{
    "NSWindow Frame SUUpdateAlert" = "970 788 620 398 0 0 2560 1415 ";
    "NSWindow Frame x11_prefs" = "487 464 584 369 0 0 2560 1415 ";
    SUHasLaunchedBefore = 1;
    SULastCheckTime = "2021-04-14 04:55:37 +0000";
    SUUpdateRelaunchingMarker = 0;
    "app_to_run" = "/opt/X11/bin/xterm";
    "cache_fonts" = 1;
    "done_xinit_check" = 1;
    "enable_iglx" = 1;
    "login_shell" = "/bin/sh";
    "no_auth" = 0;
    "nolisten_tcp" = 0;
    "startx_script" = "/opt/X11/bin/startx -- /opt/X11/bin/Xquartz";
}
```

ふむ、`enable_iglx`はtrueになっているように見える。

VMD 1.9.4a51 for MacOS X, 64-bit Intel x86 (x86_64) (Dec 21, 2020): MacOS X Big Sur fixes w/ Tcl/Tk 8.6.11

ダメだった。

結局、VMDの最新版は普通にMacに対応していたのでそれをインストールしておしまい。なんじゃらほい。

Windows版のVMD、64ビットだと起動しない。32ビットなら大丈夫。うーむ。

また、Movie Makerの仕様が変わっており、「Trajectory」を指定しないと変なことになるっぽい。

ハンズオンの準備にどえらく時間がかかってしまって、今日はそれしかできなかった。

金曜日の講義の準備。動画の設定など。
