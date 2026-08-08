---
title: "2026年7月15日"
date: 2026-07-15T00:00:00+09:00
lastmod: 2026-07-15T00:00:00+09:00
type: diary
source_month: "d202607.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

自分が昔書いたコードを修正するため、codexに読ませて「まず内容を理解してください」と言ったら、「ODR違反の可能性があります」「返り値に問題があります」「テンプレートの定義に問題があります」「テスト項目が足りません」とかボロクソに言われたんだけど。

物性研スパコンにuvを入れる。

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

PATHに`~/.local/bin`が必要だが、すでに入れてた。

```sh
git clone --recursive https://github.com/kaityo256/pycpp-parallel-pipeline.git
cd pycpp-parallel-pipeline
```

```sh
uv venv
source .venv/bin/activate
uv pip install numpy pyyaml
```

```sh
cd cpp
make
cd ..

cd cps
make
cd ..
```

```sh
python3 generate_inputs.py input.yaml 
sbatch job.sh
python3 analyze_results.py input.yaml 
```

できた。

解説も書いた。

[Pythonで準備してC++で計算する自明並列ワークフロー](https://kaityo256.github.io/pycpp-parallel-pipeline)

うーん、サンプルコードを作って、リポジトリにまとめ、それをスパコンで動作確認して、解説記事を書くまでにほぼ一日使ってしまった。

最近忙しくてこういう記事書けてないなと思ったんだけど、そもそもこういう記事を書くのは結構時間がかかっていたんだなぁ。

講義準備途中まで。査読も進めないと・・・
