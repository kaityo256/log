---
title: "2021年2月22日"
date: 2021-02-22T00:00:00+09:00
lastmod: 2021-02-22T00:00:00+09:00
type: diary
source_month: "d202102.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

[研究会](https://ccms.issp.u-tokyo.ac.jp/event/4228)のメモ。

原子間ポテンシャルの高精度モデリング
J. Behler and M. Parrinello
PRL 98 146401 (2007)

原子間力の非調和力定数の決定
熱伝導率
PRL 113, 185501 (2014)
PRB 92, 054301 (2015)
JPSJ 87, 
圧縮センシング (LASSO)を使うと、計算量が激減する。

実験データを再現するように結晶構造を決める。シミュレーティッドアニーリングでは遅いが、機械学習(ベイズ)では速い。

土師 将裕（東京大学 物性研究所）
圧縮センシングによる走査トンネル顕微鏡の高精度測定

y = A x
yが実空間 (観測量)
xが波数空間 (目的)
Aはフーリエ変換
yが欠けているときに、xを求めたい。

Y. Nakanishi-Ohno, MH, JPSJ 85, 093702 (2016)

田村 亮（東京大学大学院新領域創成科学研究科, 物質・材料研究機構）
ベイズ最適化と材料・物性研究への応用

ベイズ最適化をするアプリケーション
COMBO

ガスアトマイズ最適化
超合金粉末の最適化
R. Tamura, et al. Material & Design 198, 109290 (2020)

Liイオン伝導度最適化
K. Homma, et al. The Journal of Physical Chemistry C 124, 12865 (2020)

二元系
最高充填率
二次元二元系　9種類
三次元三元系　164種類

寺山 慧(横浜市立大学)
クライオEM密度マップからの生体分子ダイナミクス情報推定-データベース・シミュレーション・機械学習の融合

能動的な相図探索
Phys. Rev. Mater. 2019 JJAP 2019

Nature Machine Intelligence

Jackknifeの理解がおかしい。n個のデータを持つrに対して、まずbin_sizeで平均し、n/bin_sizeのデータを作ってから、それをJackknifeで一個外しては平均を取り、それに対してビンダー比を計算してもうまくいかない。詳しい人に聞いたらやっぱり間違っていた。まだ定義をきちんと理解できていない。
