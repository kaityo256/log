---
title: "2024年10月26日"
date: 2024-10-26T00:00:00+09:00
lastmod: 2024-10-26T00:00:00+09:00
type: diary
source_month: "d202410.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研システムCでMKLをリンクする方法の確認。

```sh
module purge
module load oneapi/2024.0.0
icpc -diag-disable=10441 -mcmodel=large -qmkl=parallel test.cpp -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
icpc -std=c++17 -diag-disable=10441 -mcmodel=large -DMKL -qmkl=parallel hoge.cpp -I../../  -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core
```

なんかインテルコンパイラのバグを踏んでるっぽいのだが、深堀りする時間がない。

プログラミング基礎同演習のレポート採点。今回はフラクタル画像。

年末調整。e-Taxに届いた「令和6年分住宅借入金等特別控除証明書」のXMLファイルをe-Taxからダウンロードしてアップロード、残高証明は画像でアップロード。残高証明の方は原本を提出か。
