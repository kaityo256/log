---
title: "2020年12月16日"
date: 2020-12-16T00:00:00+09:00
lastmod: 2020-12-16T00:00:00+09:00
type: diary
source_month: "d202012.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

体がどうにも重い。

会議。

メールたくさん書いた。

ARM SVEのプレディケートレジスタがわかった気がするぞ。

```cpp
#include <iostream>
#include <arm_sve.h>
#include <vector>

void show_ppr(svbool_t tp){
  std::vector<int8_t> a(64);
  std::vector<int8_t> b(64);
  std::fill(a.begin(), a.end(), 1);
  std::fill(b.begin(), b.end(), 0);
  svint8_t va = svld1_s8(tp, a.data());
  svst1_s8(tp, b.data(), va);
  for(int i=0;i<64;i++){
    std::cout << (int)b[63-i];
  }
  std::cout << std::endl;
}

int main(){
  std::cout << "svptrue_b8" << std::endl;
  show_ppr(svptrue_b8());
  std::cout << "svptrue_b16" << std::endl;
  show_ppr(svptrue_b16());
  std::cout << "svptrue_b32" << std::endl;
  show_ppr(svptrue_b32());
  std::cout << "svptrue_b64" << std::endl;
  show_ppr(svptrue_b64());
}
```

実行するとこうなる。

```txt
svptrue_b8
1111111111111111111111111111111111111111111111111111111111111111
svptrue_b16
0101010101010101010101010101010101010101010101010101010101010101
svptrue_b32
0001000100010001000100010001000100010001000100010001000100010001
svptrue_b64
0000000100000001000000010000000100000001000000010000000100000001
```

パターンを食わせるバージョンも理解できた。
