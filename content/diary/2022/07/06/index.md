---
title: "2022年7月6日"
date: 2022-07-06T00:00:00+09:00
lastmod: 2022-07-06T00:00:00+09:00
type: diary
source_month: "d202207.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

printfに4285個アスタリスクをつけたらclangが死ぬ奴、今試したら3460個になってる上に、ギリギリで試すと

```txt
test.cpp:3:3461: warning: stack nearly exhausted; compilation time may suffer, and crashes due to stack overflow are likely [-Wstack-exhausted]
```

という警告が出るな。これ、以前からあったっぽい。前回はApple LLVM version 10.0.1 (clang-1001.0.46.4)だったが、10.0.0のRelease noteにある。

ちなみに　`(((printf("Hello World\n"))))`みたいなことをすると、`clang::Parser::ParseParenExpression`というところでスタックを使い切って死ぬらしい。ふむ。

GCCは10000はいけたが、さすがに100000で死んだ。50000も死んだ。ohtakaでは34086が限界ですね。ローカルのiMacだと、g++-11で55179が限界。

arXivの投稿、endorseが必要で、そのためには当該分野にX以内にY編の論文を公開していなければならない、というものルール。そして僕はまさかのcond-mat.stat-mechのendorse権限なし。論文投稿しなさすぎ。ひどい。もっとがんばらないと・・・
