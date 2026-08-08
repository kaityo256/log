---
title: "2021年6月24日"
date: 2021-06-24T00:00:00+09:00
lastmod: 2021-06-24T00:00:00+09:00
type: diary
source_month: "d202106.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

光成さんの講義。bfloat16を知らなかった。指数部8、仮数部7の精度がいらないfloat。

float 符号1、指数8、仮数部、23bit。

movのゼロ化マスク{z}の意味を初めて知った。
{z}がついていると、マスクビットがたっていないところはゼロクリアされる。なければそのまま。

対数の桁落ちの問題をSIMD化するのか。すごい。

movprfx命令(補助命令) 積和演算の

そうか。テイラー展開がfmaddでできるのか。SVEならfacgeで一発。

やっぱりテーブルルックアップでいけるのか。
テーブル引きのSIMD化にはgather命令が必要。

富岳のハードレジスタは128個。見えるのは32個。

predありの命令はmergeをするから、dstにあっても依存関係を持つ。

movprfxを挿入で依存関係を切る。

Intel AMX。8個のレジスタ。1個1KiB。マジか。

光成さんの講義、面白かった。

本読み輪講。ゴム弾性の話。

論文の図の作成。図はあとひとつかな。
