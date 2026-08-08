---
title: "2023年9月23日"
date: 2023-09-23T00:00:00+09:00
lastmod: 2023-09-23T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

矢上祭。人と会う約束があったので初めて参加してみたが、わりと親子連れがいる感じ。

昨日のコード、もっとスッキリさせた。

```cpp
#include <cstdio>
int main(){
  int a = 0, b = 0;
  a = --a + ++a + ++a;
  b = ++b + ++b + a;
  for (int i=1;i<16;i++){
    if (i%b==0){
      printf("%s\n",a?"buzz":"fizz");
    }else{
      printf("%d\n",i);
    }
  }
}
```
