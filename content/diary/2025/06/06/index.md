---
title: "2025年6月6日"
date: 2025-06-06T00:00:00+09:00
lastmod: 2025-06-06T00:00:00+09:00
type: diary
source_month: "d202506.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研スパコンでのLAMMPSのバルクジョブのサンプルコード書いた。

[LAMMPS Bulk Job Sample](https://github.com/kaityo256/lammps_bulkjob_sample)

すぐできると思ったが、思ったより時間かかったな。シェルスクリプトの実行時間を知るための`SECONDS`変数を初めて知った。bashの特殊変数のようだ。zshにもあるみたい。

lammpstrjの解析用C++ヘッダも途中まで作った。

[kaityo256/lammpstrj-parser](https://github.com/kaityo256/lammpstrj-parser)

関数オブジェクトやコールバック関数みたいなやつ、最近はどうするんですか？って聞いたら`std::function`ですって。C++11らしい。何も知らんかった。
