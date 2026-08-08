---
title: "2021年2月27日"
date: 2021-02-27T00:00:00+09:00
lastmod: 2021-02-27T00:00:00+09:00
type: diary
source_month: "d202102.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

JackknifeのC++版の実装。Pythonから入るとSTLのコンテナ操作系の使いづらさが際立つ。

```cpp
std::transform(r.begin(), r.end(), r2.begin(), [](double x) { return x * x; });
```

みたいな奴、

```cpp
std::transform(r, r2, [](double x) { return x * x; });
```

でいいじゃん。もっというなら

```cpp
auto r2 = std::transform(r, [](double x) { return x * x; });
```

でいいじゃんね。

`std::accumulate`で、`double`を積算するのに初期値に「0」を入れて、積算が`int`で行われている、というバグを入れてたのにしばらく気づかなかった。こんなの。

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
  std::vector<double> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  std::cout << std::accumulate(v.begin(), v.end(), 0) << std::endl;
  std::transform(v.begin(), v.end(), v.begin(), [](double x) { return 0.5 * x; });

  std::cout << std::accumulate(v.begin(), v.end(), 0) << std::endl;  // => 25
  std::cout << std::accumulate(v.begin(), v.end(), 0.0) << std::endl; // => 27.5
}
```

初期値に0と0.0を入れた時で答えが変わる。最初のテストでは整数しか入れてなかったので答えがあってて見落とした。コンパイラは何も言わないし、計算も普通にできるんだけど、微妙に答えがおかしくなるのですごくイヤなバグ。
