---
title: "2022年12月21日"
date: 2022-12-21T00:00:00+09:00
lastmod: 2022-12-21T00:00:00+09:00
type: diary
source_month: "d202212.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

会議と打ち合わせ。

Minimal hitting setsのリストアップアルゴリズムについて質問が来た。[これ](https://github.com/kaityo256/mhs_cpp)を見て質問してきたらしい。

質問内容は

e ={{1,2}{2,3,7},{3,4,5},{4,6},{6,7,8},{7}}

についてのhitting setsを求めよ、という問題について、詳しくアルゴリズムの説明をしてほしいというもの。せっかくなので回答をこっちにも残しておこう。

```txt

Let me summarize the notation first.

HS: hitting set
MHS: minimal hitting set

Consider the bit representation of the inputs as follows.

00000011 e1 = {1,2}
01000110 e2 = {2,3,7}
00011100 e3 = {3,4,5}
00101000 e4 = {4,6}
11100000 e5 = {6,7,8}
01000000 e7 = {7}

Consider a subset k-set containing up to ek.
For example, 1-set = {e1}, 2-set = {e1, e2}, and so on.

We define k-HS and k-MHS as follows.

k-HS: HS for k-set
k-MHS: MHS for kset.

Our goal is to enumerate 7-MHS. The key idea is to construct k-MHS from (k-1)-MHS.

The 1-MHS is easy. The following two bit strings are 1-MHS.

h1 = 00000001
h2 = 00000010

We recursively construct the 2-MHS from here.
Suppose we take h1. h1 is not 2-MHS. So we add a bit to it.

h1' = 00000011

h1' is HS of 2-set, but it is not 2-MHS because it is still a hitting set, even if we remove a bit from it. We, therefore, reject h1'.

Next, we consider h2. This is 2-MHS because we cannot remove any bits from it. So we adopt h2, and continue to find 3-MHS from it.

The algorithm to enumerate MHS is as follows.

1. Enumerate 1-MHS (it is easy).
2. For each element of k-MHS, check whether it is (k+1)-MHS.
3. If t is (k+1)-MHS, then we continue to search recursively.
4. If t is not (k+1)-MHS, then we add a bit (t->t') so that t' becomes k-HS. Then check whether t' is (k+1)-MHS. If t' is not (k+1)-MHS, then we reject it. If t' is (k+1)-MHS, we continue searching recursively.
5. k -> k +1 and goto 2.

It takes some ingenuity to determine whether a given bit string is k-MHS.

The function check_minimal in mhs.cpp is a naive implementation. But check_minimal2 is a more efficient one adopting the idea of critical hyperedge. But it is not essential.

I hope the above explanation helps you.
```

うげ、数理物理ってクォーター(月4金4)か。

* 出講希望
    * プログラミング基礎同演習は11月に出してた。
    * 数理物理：黒板を要望。
    * 物理情報工学ソフトウェア開発演習：必要機材は「パソコン画面投影(PCご本人用意)」と「パソコン教室(デスクトップPC)」で、頻度は「ほぼ毎回利用する」。
    * シミュレーション工学：黒板、ホワイトボード指定なし。必要機材は「パソコン画面投影(PCご本人用意)」のみ。頻度は「ほぼ毎回利用する」。

* シラバス入力
    * プログラミング基礎同演習は手で入力したが、昨年度から変更がなかったのでコピーでよかったな。
    * 物理情報工学ソフトウェア開発演習は昨年度と変更なし。コピーでOK。
    * シミュレーション工学：昨年度のコピーをして、予定と変更したところを修正。

[量子力学を学ぶための解析力学入門 増補第2版 (KS物理専門書)](https://www.amazon.co.jp/dp/4061532413)を注文した。やはり最後は量子力学につなげようと思って。

数理物理のシラバスはもうちょっと考える。

修士論文発表会のプログラム。参加メンバーの最終チェック。よし、完全に把握した。明日にはプログラムを作れるはず。

明日の午前中も会議か。
