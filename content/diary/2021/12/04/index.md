---
title: "2021年12月4日"
date: 2021-12-04T00:00:00+09:00
lastmod: 2021-12-04T00:00:00+09:00
type: diary
source_month: "d202112.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学科わけ説明会。物情はかなり頑張っていたのではないか。委員長のリーダーシップ(とセンス)が素晴らしい。

ただ、ずっと立ちっぱなし喋りっぱなしで疲れた。

```cpp
int a;
int b = ++a + ++a + ++a;
```

とあったときに、bがいくつになるか。gccでは10、clangでは9になる。

なぜgccで10になるかは、コンパイラに聞いてみるとわかる。

```cpp
int func(int a){
  return ++a + ++a + ++a;
}
```

というコードを書いて、抽象構文木をダンプしてやる。

```sh
gcc-10 -c -fdump-tree-all-graph test.c 
```

Macなのでgcc-10と指定している。すると、コンパイラがこのコードをどのように解釈したかが表示される。

まず、test.c.004t.originalがこうなる。

```cpp
int func(int a){
  return ( ++a +  ++a) +  ++a;
}
```

先に、左の`+`をまとめて実行する。これを`tmp1`でうけよう。

```cpp
int a = 1
int tmp1 = ++a +  ++a;
return tmp1 + ++a;
```

`tmp1 + ++a`は`tmp2`で受けよう。

```cpp
int a = 1
int tmp1 = ++a +  ++a;
int tmp2 = tmp1 + ++1;
return tmp2;
```

さて、前置インクリメントなので、`++a +  ++a`の+の実行前にインクリメントを実施する。

```cpp
// int tmp1 = ++a +  ++a;
a = a + 1;
a = a + 1;
int tmp1 = a + a;
int tmp2 = tmp1 + ++a;
return tmp2;
```

次に、`tmp1 + ++a`も同様に、先にインクリメントを実施する必要がある。

```cpp
// int tmp1 = ++a +  ++a;
a = a + 1;
a = a + 1;
//int tmp2 = tmp1 + ++a;
a = a + 1;
int tmp2 = tmp1 + a;
return tmp2;
```

最終的に、関数はこうなった。

```cpp
int func(int a){
  a = a + 1;
  a = a + 1;
  int tmp1 = a + a;
  a = a + 1;
  int tmp2 = tmp1 + a;
  return tmp2;  
}
```

というわけで、`a=1`の時には `++a + ++a + ++a = 3 + 3 + 4 = 10`になる。

clangの場合は9になる。どう解釈したかは、中間コードを見るとわかる。

```cpp
define i32 @func(i32 %0) #0 {
  %2 = %0  // %2 = 1
  %3 = %2  // %3 = 1
  %4 = %3 + 1 // %4 = 2
  %2 = %4     // %2 = 2
  %5 = %2     // %5 = 2
  %6 = %5 + 1 // %6 = 3
  %2 = %6     // %2 = 3
  %7 = %4 + %6 // %7 = 2 + 3 = 5
  %8 = %2      // %8 = 3
  %9 = %8 + 1  // %9 = 4
  %2 = %9
  %10 = %7 + %9 // %10 = 5 + 4
  return %10
}
```

つまり、clangの場合は`++a + ++a + ++a = 2 + 3 + 4 = 9`となる。

そもそも`++a + ++a`が、gccは6、clangは5になる。

gccは、

```cpp
a = a + 1
a = a + 1
return a + a;
```

と解釈する。clangは、

```cpp
%2 = %0 // %2 = 1
%3 = %2 // %3 = 1
%4 = %3 + 1 // %4 = 2
%2 = %4 // %2 = 2
%5 = %2 // %5 = 2
%6 = %5 + 1 // %6 = 3
%2 = %6
%7 = %4 + %6 // 2 + 3 = 5
```

つまり、

```cpp
tmp1 = a + 1
a = tmp1
tmp2 = a + 1
a = tmp2
return tmp1 + tmp2;
```

つまり、clangは、`++a`を、`tmp = a + 1;a = tmp`という形に受ける。

```cpp
int b = ++a + ++a;
```

は、

```cpp
tmp1 = a + 1;
a = tmp1;
tmp2 = a + 1;
a = tmp2;
int b = tmp1 + tmp2;
```

とバラす。gccは、

```cpp
a = a + 1
a = a + 1
int b = a + a;
```

とするので6になる。なるほど。

まとめると、`++a + ++a`とあった場合、GCCは、+の両側のインクリメント演算子を解決してからしてから加算を実行するが、clangは`++a`を`tmp = a + 1;a = tmp`にバラす。

理解できたかどうか、もう一度`++a + ++a + ++a`でやってみよう。

GCCの場合、まず、カッコをつける。

```cpp
return (++a + ++a) + ++a;
```

カッコをtmp1で受ける。

```cpp
int tmp1 = ++a + ++a;
return tmp1 + ++a;
```

`tmp1`を評価する際、まずインクリメント演算子を解決する。

```cpp
a = a + 1;
a = a + 1;
int tmp1 = a + a;
return tmp1 + ++a;
```

`tmp1 + ++a`のインクリメント演算子を解決する。

```cpp
a = a + 1;
a = a + 1;
int tmp1 = a + a;
a = a + 1:
return tmp1 + a;
```

以上から3+3+4=10になる。

clangの場合。

`++a`を`tmp = a + 1;a = tmp;`に変換。

```cpp
int tmp1 = a + 1;
a = tmp1;
return tmp1 + ++a + ++a;
```

次の`++a`も同様に変換。

```cpp
int tmp1 = a + 1;
a = tmp1;
int tmp2 = a + 1;
a = tmp2;
return tmp1 + tmp2 + ++a;
```

また変換。

```cpp
int tmp1 = a + 1;
a = tmp1;
int tmp2 = a + 1;
a = tmp2;
int tmp3 = a + 1;
a = tmp3;
return tmp1 + tmp2 + tmp3;
```

以上から2+3+4 = 9になる。うん、完全に理解した。
