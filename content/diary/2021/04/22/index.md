---
title: "2021年4月22日"
date: 2021-04-22T00:00:00+09:00
lastmod: 2021-04-22T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物理情報工学特別講義の動画が大きい。

```sh
ffmpeg -i aiyoshi01.mp4 -crf 32 aiyoshi01_low.mp4
```

これで2.48GB→167.4MB。しかし、crf 32はさすがに大きすぎた(粗すぎた)。28で再挑戦。

```sh
ffmpeg -i aiyoshi01.mp4 -crf 28 aiyoshi01_low.mp4
```

2.48GB→237MB。良さげかな。もう少し下げても良さそう。

Linuxのカーネルに意図的にバグを入れたパッチを出して、コミュニティーがどのように対応するかを調べるという[研究](https://github.com/QiushiWu/qiushiwu.github.io/blob/main/papers/OpenSourceInsecurity.pdf)をしたミネソタ大学がLinux出禁に。

LinuxカーネルのメンテナであるGregは[カンカン](https://lore.kernel.org/linux-nfs/YH%2FfM%2FTsbmcZzwnX@kroah.com/)。

[ミネソタ大学の声明](https://twitter.com/UMNComputerSci/status/1384948683821694976/photo/1)

```txt
Leadership in the University of Minnesota Department of Computer Science & Engineering learned today about the details of research being conducted by one of its faculty members and graduate students into the security of the Linux Kernel.

The research method used raised serious concerns in the Linux Kernel community and, as of today, this has resulted in the University being banned from contributing to the Linux Kernel.

We take this situation extremely seriously. We have immediately suspended this line of research. We will investigate the research method & the process by which this research method was approved, determine appropriate remedial action, & safeguard against future issues, if needed.

We will report our findings back to the community as soon as practical. 

Sincerely,

Mats Heimdahl, Department Head
Loren Terveen, Associate Department Head
```

ハンズオン。MarkdownとLaTeX記法。

ミネソタの件、PIによる[声明](https://github.com/QiushiWu/qiushiwu.github.io/blob/main/papers/OpenSourceInsecurity.pdf)。

研究室ミーティング。担当は僕で「科研費の通し方」。自分でも偉そうなタイトルだと思う。まぁ、知っていることは全部伝えたい。
