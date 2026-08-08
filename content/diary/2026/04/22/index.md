---
title: "2026年4月22日"
date: 2026-04-22T00:00:00+09:00
lastmod: 2026-04-22T00:00:00+09:00
type: diary
source_month: "d202604.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

明日の発表スライド完成したことにする。LightGBMの理解の準備のために勾配ブースティングと決定木を説明する。

BitLockerで暗号化されたDynabookを再インストールしようとしたが、Intel Rapid Storage Technologyでディスクがマウントされており、通常のWindowsインストーラからはディスクが見えない。で、ドライバファイルをダウンロードしたが、自己解凍exe。あまり実行したくない。

で、チャッピーに聞いたら「7zipで解凍できますよ」マジで？

```sh
$ 7z x TCH0959000A.exe

7-Zip [64] 17.05 : Copyright (c) 1999-2021 Igor Pavlov : 2017-08-28
p7zip Version 17.05 (locale=utf8,Utf16=on,HugeFiles=on,64 bits,20 CPUs x64)

Scanning the drive for archives:
1 file, 8877768 bytes (8670 KiB)

Extracting archive: TCH0959000A.exe
(snip)
Everything is Ok

Folders: 2
Files: 31
Size:       21331486
Compressed: 8877768
```

マジだ。これでDriversというフォルダができるので、そこにVMDのドライバファイルがある。

これをブート用USBにコピー。

* ブート用USBを挿入した状態で起動。タッチパッドが認識しないのでマウスが必須。
* 起動時に「0(をわ)キー」を連打(テンキーじゃないほう)
* ダイアログがでてくるのでY
* 「オプションの選択」で「デバイスの使用」→USB Memory
* 再起動してWindows 11セットアップ画面に
* 言語設定を選択→次へ
* キーボード設定を選択→次へ
* セットアップオプションの選択。「WIndows 11のインストール」を希望し、ファイル、アプリなどが消えることに同意して次へ。
* ライセンスに同意
* Windows 11をインストールする場所の選択：ここで内臓ディスクが見えない。「ドライバーのロード(L)」を選んでIntel VMDドライバをロード。
* Windows 11をインストールする場所の選択：に戻ってくる。ディスク1パーティション3に種類「第1」が現れるのでそれを選択。そのままではBitLockerで暗号化されててインストールできないので「パーティションの削除」により未割当領域に。それを選んだまま「次へ」
* インストール準備完了：「インストール(I)」

初期化できた！なんかひと仕事終えた感。

来客。頑張ってください。

理事会の仕事とか、ネットワーク委員の仕事とか。なんとか。かんとか。

無限に仕事が増えていくが、なんとか論文再投稿のための論文を読んでいる。

あと、本の執筆も少しずつ始めた。
