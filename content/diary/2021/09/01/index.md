---
title: "2021年9月1日"
date: 2021-09-01T00:00:00+09:00
lastmod: 2021-09-01T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

9月になってしまった。

科研費の独立基盤形成の書類を一つ提出。これであとひとつのはず。

健康診断の予約したぞ。

久しぶりに迷惑メールみたら、8月16日に友人から久しぶりに来てたメールが迷惑メールに振り分けられているのを発見。Gmailの迷惑メール判定、もう信頼できない(偽陽性が多すぎる)ので、数日に一度は見に行かないとダメだな……

git rebaseの説明をZennに書いた。こうしてトピックごとにZennに書いて、思考を整理してから講義ノートにまとめていくスタイル。

Linuxのコマンドグルーピングというものを知った。echoの結果とcatの結果を、この順番でファイルに落としたい。

普通にやるなら中間ファイルが必要。

```sh
echo "Hoge" > head.txt
cat head.txt tail.txt > total.txt
```

しかし、中括弧で囲むとこんなことができる。

```sh
{echo "Hoge"; cat tail.txt;} > total.txt
```

これで、Gitのハッシュを調べることができる。こんなファイルを考える。

```txt
Hello Git!
```

Gitのハッシュを調べる。

```sh
$ git hash-object test.txt
106287c47fd25ad9a0874670a0d5c6eacf1bfe4e
```

Gitのハッシュはsha1sumなのだが、このまま食わせると違うものになる。

```sh
$ shasum test.txt
871fc2d049fbfab104eeca13c37ff938a1ffaf3d  test.txt
```

これは、頭に`blob filesize\0`というヘッダがついているから。filesizeはファイルサイズ。`\0`はヌル文字。

ファイルサイズを調べる。

```sh
$ wc -c < test.txt
      11
```

11バイトなので、`blob 11\0`をヘッダとして追加し、それを`shasum`にかける。

```sh
$ { echo -en 'blob 11\0'; cat test.txt; } | shasum
106287c47fd25ad9a0874670a0d5c6eacf1bfe4e  -

$ git hash-object test.txt
106287c47fd25ad9a0874670a0d5c6eacf1bfe4e
```

よしよし、無事に一致した。
