---
title: "2026年2月24日"
date: 2026-02-24T00:00:00+09:00
lastmod: 2026-02-24T00:00:00+09:00
type: diary
source_month: "d202602.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

PDFのパスワードをpdftkで外そうとしたら、

```sh
$ pdftk input.pdf input_pw password output output.pdf
Warning: Using a password on the command line interface can be insecure.
Use the keyword PROMPT to supply a password via standard input instead.
Error: Invalid PDF: unknown.encryption.type.r
Error: Failed to open input PDF file: 
   input.pdf
Errors encountered.  No output created.
Done.  Input errors, so no output created.
```

と言われた。このPDFのパスワードにPDFTKが対応していないらしい。

qpdfで対応可能。

```sh
brew install qpdf
qpdf --password='password' --decrypt input.pdf output.pdf
```

pipによるインストール、

```sh
python3 -m pip install https://github.com/watanabe-appi/simple_rbm.git
```

ではエラーが出て

```sh
python3 -m pip install git+https://github.com/watanabe-appi/simple_rbm.git
```

としなければならない。最初、Gitでやっていたのをhttpsに変えた時にミスったかな？PRに感謝。

長らく懸案だった「行間解析力学」の[正誤表](https://kaityo256.github.io/classical_mechanics/errata/index.html)を作った。

数式をどうするか迷ったが、結局「一行でいける場合や分数がない場合」はインラインで、複雑な場合はLaTeXiTで作ることにした。

査読まで手が回らなかった・・・

そろそろ春の学校の準備もしないと。
