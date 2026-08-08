---
title: "2024年10月3日"
date: 2024-10-03T00:00:00+09:00
lastmod: 2024-10-03T00:00:00+09:00
type: diary
source_month: "d202410.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

研究室ミーティング。

以下のPythonスライド修正。

* Chainerへの言及を消す
* 描画の原点が左上であることを伝える

学生さんに紹介用論文を紹介した。

関数内で大きな配列を宣言する奴、クラス定義でも起きるというのは罠だな。

```cpp
class Hoge{
  void func(){
    double large_array[HUGE_NUMBER];
  }
};
```

みたいな奴を、

```cpp
void fuga(){
  Hoge h;
}
```

みたいに宣言するとスタックを使い切る問題。どこかにメモっておこう。
