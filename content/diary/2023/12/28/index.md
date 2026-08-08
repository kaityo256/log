---
title: "2023年12月28日"
date: 2023-12-28T00:00:00+09:00
lastmod: 2023-12-28T00:00:00+09:00
type: diary
source_month: "d202312.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

```sh
$ icpc

Error: A license for Comp-CL is not available (-16,287).

License file(s) used were (in this order):
**  1.  /opt/intel/compilers_and_libraries_2020.0.166/linux/licenses
**  2.  /opt/intel/licenses/COM_L__CPPFOR_GDXV-5J47RJPC.lic
**  3.  /opt/intel/licenses/l_5J47RJPC.lic
**  4.  /opt/intel/licenses/server.lic
**  5.  /opt/intel/licenses/watanabe-login.lic
**  6.  /home/yamamoto/intel/licenses
**  7.  /opt/intel/compilers_and_libraries_2019.4.243/linux/bin/intel64/../../Licenses
**  8.  /home/yamamoto/Licenses
**  9.  /Users/Shared/Library/Application Support/Intel/Licenses
**  10.  /opt/intel/compilers_and_libraries_2019.4.243/linux/bin/intel64/*.lic

Please refer http://software.intel.com/sites/support/ for more information..

icpc: error #10052: could not checkout FLEXlm license
```

またIntelコンパイラのライセンスサーバが死んだ。日記にgrepかけて復活手順を確認。パスを隠す意味もないだろうから、復活の手順を書いておく。

ライセンスサーバのプロセス番号とコマンドの確認。

```sh
$ sudo ps aux | grep lmgrd
root       4426  0.0  0.0  25572    80 ?        Sl    8月21   3:04 /opt/intel/licenseserver/lmgrd -c /opt/intel/licenses/COM_L__CPPFOR_GDXV-5J47RJPC.lic -l /opt/intel/licenseserver/flexnet_logfile.txt
```

ライセンスサーバを殺す。

```sh
sudo kill -KILL 4426
```

ライセンスサーバ再起動。psで確認したコマンドをそのまま入力。

```sh
/opt/intel/licenseserver/lmgrd -c /opt/intel/licenses/COM_L__CPPFOR_GDXV-5J47RJPC.lic -l /opt/intel/licenseserver/flexnet_logfile.txt
```

```sh
$ icpc --version
icpc (ICC) 19.0.4.243 20190416
Copyright (C) 1985-2019 Intel Corporation.  All rights reserved.
```

復活。日記書いてて良かった。

会議があったのを完全に失念していた。うげ。
