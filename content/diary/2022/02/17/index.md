---
title: "2022年2月17日"
date: 2022-02-17T00:00:00+09:00
lastmod: 2022-02-17T00:00:00+09:00
type: diary
source_month: "d202202.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

金子先生も清水先生も最終講義か・・・

* 【最終講義】金子 邦彦 教授 [やり残したことなど：カオス、複雑系、普遍生物学、それから](https://www.c.u-tokyo.ac.jp/info/news/events/20220203100000.html)
* 【最終講義】清水 明 教授 [謎に惹かれて基礎の森](https://www.c.u-tokyo.ac.jp/info/news/events/20220203110000.html)

昨年の卒論、製本が上がってきたので受け取った。

研究室ミーティング。ANNNIモデルの厳密対角化の結果と、機械学習によるタンパク質の構造予測の話。厳密対角化屋さん、古典系での結果を見るのは久しぶりな気がする。タンパク質の構造予測は実際に合成して確認するのはすごい。

重い腰を上げて新しいMacのセットアップ。アップデートがかかっているうちに、古いMacのデータの整理。主にsvn管理されていないファイルの削除など。

PCのデータを調べてたら、たら、昔のサーバがリモートになっているsvnリポジトリを発見。死ぬほど久しぶりにsvnadminを触る。

```sh
svnadmin create rep_name
```

```sh
svn co svn+ssh://username@servename.jp/home/username/rep_name local_rep
```

学生さんに「左利きなんだね」と言ったら「それ言われるの4回目です」。正直すまんかった。
