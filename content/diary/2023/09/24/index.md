---
title: "2023年9月24日"
date: 2023-09-24T00:00:00+09:00
lastmod: 2023-09-24T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

矢上祭。子供を連れて来てみた。KCSのゲームを気に入ったっぽい。

未定義動作でFizzBuzz、そういえば関数の引数の処理の順番も処理系依存だな、と思ったので、[そっちで作ってみた](https://zenn.dev/kaityo256/articles/fizzbuzz_undefined2)。

コードはこんな感じ。

```c
#include <stdio.h>

int a = 0;
int f() {
  a += 1;
  return a;
}
int g() {
  a *= 2;
  return a;
}
int h(int a1, int a2) {
  return a1 * a2;
}

int main() {
  a = h(f(), g());
  for (int i = 0; i < 16; i++) {
    if (i % (a + 3) == 0) {
      printf("%s\n", a ? "buzz" : "fizz");
    } else {
      printf("%d\n", i);
    }
  }
}
```

本質はここ。

```c
  a = h(f(), g());
```

これが、`h`から処理されるか`g`から処理されるかが処理系依存。x86のGCCとAarch64のGCCの意見が変わるので、それで結果が変わる。

この話、C++ MIXで話したら面白いかな、と思ったけど、2020年1月29日のC++ MIX #7が最後っぽいですね。僕が話したのは#6。C++ MIXの動画の中で、僕の発表のがダントツに再生数が多いのが密かに自慢。

こういうアホな話をする場が無いのは寂しいなぁ。

昔の日記を少しサルベージした。そこで[Menthas](https://menthas.com/)というサービスを使っていたことを思い出し、もう一度アクセスしてみた。

今は、プログラミング関係の話題はほとんどZennのトップページで摂取してるなぁ。

学生さんの論文、再投稿した。JCPはいつのまにか「Highlight Image」みたいなのを要求するようになった。

* Required Highlight Image
  * A highlight image is required with your submission. It may be a figure from your paper or another image you create that reflects your work.
  * This image should measure 8.0139 in. wide X 6.2739 in. high and be a minimum of 300 dpi.
  * Acceptable file types for the highlight image are EPS, TIFF, and JPEG.
  * Your highlight image will display above your article title online.
  * If your paper is selected as the cover article, your highlight image will serve as the cover image for the journal issue.

だそうな。これ要求するの、Acceptの時で良いと思うんだけどな。
