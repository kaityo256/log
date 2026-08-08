---
title: "2019年4月26日"
date: 2019-04-26T00:00:00+09:00
lastmod: 2019-04-26T00:00:00+09:00
type: diary
source_month: "d201904.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

WindowsにAnacondaを入れる。

Downloadにいって「Windowsタブ」にしてから、「Python 3.7 version」のDownloadをクリック。
Anaconda3-2019.03-Windows-x86_64.exeをダブルクリックしてインストール。死ぬほど時間がかかる。
また、初回起動もかなり時間がかかるので、あらかじめ実行しておくと良い。

Newport PMManagerを入れてみる。1918-Rはもうobsolete
https://www.newport.com/p/1919-R

ThorlabのステッピングモータをPythonから制御したければ、APT System Software。

APT 32-Bit Software for 64-BIT Windows
setup.exeを実行

Anaconda Shellを使って、 thorlabs_apt-masterのsetup.pyを実行

python setup.py install

だめだ、APT.dllが読めない。

Thorlabs Kinesisの64bit-64bitをダウンロード。

Windowsにおけるdllの検索パスはLD_LIBRARY_PATHではなくPATHらしい。

Cocoonでメニューが表示されない。php-xmlがないのが原因。

sudo yum install --enablerepo=remi,remi-php73 php-xml
