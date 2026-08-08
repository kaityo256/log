---
title: "2025年3月11日"
date: 2025-03-11T00:00:00+09:00
lastmod: 2025-03-11T00:00:00+09:00
type: diary
source_month: "d202503.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

サーバに公開鍵認証でログインできず、なぜかパスワードのみ。調べたらSELinuxのせいだった。本当になんなのこれ？

Macでtensorflowをinstallできない。Pythonのバージョン上限(下限ではなく)があるらしい。仮想環境を3.11を明示的に指定して作る必要がある。

```sh
python3.11 -m venv .venv
source .venv/bin/activate
python3 -m pip install tensorflow Pillow pickles 
```

塩漬けになっていた論文に朱入れ。これから加速していきたい。

GPGPUの存在判定をcupyのimportの成否で確認していたが、Google ColabではランタイムがCPUでもcupyがimportできるためにバグっていた。なので、GPGPUの自動判定をやめて、ユーザに明示的に指定させる方法に修正。

あと、Python3.9から非推奨となったtypist.Dictを消そうとしたら、物性研のPythonが古くて(3.6)駄目だった。

あと、logging消したり、メッセージ修正したり。

学生さんの進捗がすごくて、対応が後手に回っている。うれしい悲鳴だが。
