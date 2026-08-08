---
title: "2022年8月23日"
date: 2022-08-23T00:00:00+09:00
lastmod: 2022-08-23T00:00:00+09:00
type: diary
source_month: "d202208.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

絵を描くAI、midjournyが話題。ラジオでも紹介されていた。「絵描きの仕事がなくなる」という懸念に対して、「写真が登場した時のようになるのでは」というコメントが興味深かった。写真の登場により、例えば新聞用の写実的な絵を描く、といった仕事はなくなったが、絵描きはより自由になったとも言える。

突然電源が切れて、しばらく起動しなくなったiMac。今日は無事に使えているが、怖いので修理に出した。再現不可能で帰ってくるかもなぁ。

一方、再インストールに必ず失敗するMacBook Pro。起動ディスクからのインストールを試みる。

まずはMac起動ディスク作成。AppStoreでmacOS Montereyをダウンロード(15分くらいかかる)。インストールが起動するが中断。

そのあとターミナルで

```sh
sudo /Applications/Install\ macOS\ Monterey.app/Contents/Resources/createinstallmedia --volume /Volumes/MacBoot
```

ちなみにMacBootはUSBのボリューム名。めちゃくちゃ時間かかるな。

Montereyだと認識せず。Big Surの起動ディスクを作り直す。また時間かかるなぁ。

```sh
sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --volume /Volumes/MacBoot
```

パスに空白を入れられるようにするって、本当に必要だったかなぁ？

起動ディスクを作成中、なんか気になって他の作業ができない・・・

ダメだ。起動ディスクは完成して、ディスクユーティリティからも見えるのに、起動ディスクとして認識しない。あきらめて修理に出した。

いま気が付いたが、M1 Macだった。IntelとM1で起動ディスクの作り方違ったのかも。まぁいいや。

明日のスライド作った。いつもギリギリだなぁ。ギリギリに作ることを戒めておきながらこれだもんな。

査読レポート来た。かなりPositive。良かった。
