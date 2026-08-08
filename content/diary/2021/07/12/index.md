---
title: "2021年7月12日"
date: 2021-07-12T00:00:00+09:00
lastmod: 2021-07-12T00:00:00+09:00
type: diary
source_month: "d202107.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

その、「禁煙にはこうすれば良いですよ。自分は喫煙したことないですけど」みたいな「アドバイス」をしたがる人が多いのはなぜだろうか。なんか、「なにかの役に立ちたい。でも自分には特にスキルはない」という人が、焦ってなにかをしようとするとろくなことがない気がする。デマの拡散とか。

最近著しく集中力を欠いている。集中力を欠くと、↑こういうこと(ネットの闇成分への反応)を言いがちなので良くない。自覚はあるんですよ。

追加予算執行の確認した。メールもした。

WSL2のDISPLAY、hostname.mshome.netで取れるという記事をみて試したんだけど、hostname + mshome.netで取れるIPアドレスが172.23.96.1とかで、それだとなぜうちの環境ではダメ。192.168の、Windows側のIPじゃないとXが通じなかった。172はWSL側のIPアドレスだと思うんだけど、そのあたりの関係がどうなっているかよくわかってない。

C++の一様初期化というのを知った。C++11で導入。こんなコードを考える。

```cpp
#include <cstdio>

struct Hoge {
};

int main(){
  Hoge h();
}
```

これは、おそらく無引数のクラス`Hoge`の型の変数`h`の宣言を意図しているが、実際には`Hoge`を返す関数`h`のプロトタイプ宣言とみなされる。clang++は昔から、gccは11から警告`-Wvexing-parse`が導入、デフォルトでオンなっているため、警告が出る。

```txt
prog.cc: In function 'int main()':
prog.cc:7:9: warning: empty parentheses were disambiguated as a function declaration [-Wvexing-parse]
    7 |   Hoge h();
      |         ^~
prog.cc:7:9: note: remove parentheses to default-initialize a variable
    7 |   Hoge h();
      |         ^~
      |         --
prog.cc:7:9: note: or replace parentheses with braces to aggregate-initialize a variable
0
```

C++11から、コンストラクタ呼び出しに中括弧を使える。

```cpp
#include <cstdio>

struct Hoge {
};

int main(){
  Hoge h{};
}
```

これで紛れがなくなる。他にも使い捨て構造体を作るのに便利らしい。なるほど。
