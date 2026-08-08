---
title: "2019年5月10日"
date: 2019-05-10T00:00:00+09:00
lastmod: 2019-05-10T00:00:00+09:00
type: diary
source_month: "d201905.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

KLLの新任者研究推進費、申請した。危なかった。

伊藤サプライにシュレッダーのカタログ依頼した。

Tholabsのステッピングモータを動かすためには、Windowsの環境変数に

C:\Program Files\Thorlabs\Kinesis

が必要。他に設定がある場合は、直前にセミコロンを入れて区切ること。

次、Newport Power Meter。電源を入れてからUSBに挿してみる。
PMManager 3.31が入っている状態だったが、デバイスドライバがインストールされない、と表示される。

[ftp://download.newport.com/Software/Newport_USB_Driver/](ftp://download.newport.com/Software/Newport_USB_Driver/)

から、「Newport USB Driver 5.0.8.zip」をダウンロード、展開。中のSetup.exeを実行。
インストール前にすべてのハードウェアを切り離して置くこと。
64bit mode on a 64bit Operating Systemを選ぶ。

インストール完了後にUSBを接続し、「Newport Power Meter　デバイスドライバーソフトウェアが正しくインストールされました」と表示されれば成功。
PMManagerを起動してみる。だめだ。デバイスが見つからない。1919-Rには接続できるが、1918-Rは対象外のようだ。

[この記事](http://juluribk.com/2015/04/04/newport-1918-power-meter-with-python/)を参考に。

プロダクトIDを調べる。
Windowsのデバイスマネージャで、「Universal Serial Bus Devices」のNewport Power Meterを見る。
0xCEC7だった。
