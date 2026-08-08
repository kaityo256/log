---
title: "2024年6月4日"
date: 2024-06-04T00:00:00+09:00
lastmod: 2024-06-04T00:00:00+09:00
type: diary
source_month: "d202406.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理の録画を確認したが、音が駄目だった。ワイヤレスマイクが必要。RODE Wireless GOが良いらしいが、さすがに高い(4万〜5万)。いろいろ調べてサンワダイレクトの400-MCW001を頼んでみた。

メモ。古い環境でPython仮想環境を構築する方法。pip無しで仮想環境を構築してから、後でpipをローカルにインストールする。

```sh
python3 -m venv myenv --without-pip  
source myenv/bin/activate 
wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
python3 get-pip.py
```

NumPyが裏でなんスレッド使っているか確認。`threadpoolctl`をインストール。

```sh
python3 -m pip install threadpoolctl ipython
```

ipython3上で以下を実行。

```txt
from threadpoolctl import threadpool_info
import numpy as np
threadpool_info()
```

計算ノード。

```txt
[{'user_api': 'blas',
  'internal_api': 'openblas',
  'prefix': 'libopenblas',
  'filepath': '/home/watanabe/github/simple_rbm/myenv/lib/python3.6/site-packages/numpy.libs/libopenblasp-r0-09e95953.3.13.so',
  'version': '0.3.13',
  'threading_layer': 'pthreads',
  'architecture': 'SkylakeX',
  'num_threads': 40}]
```

AMD EPYC

```txt
[{'user_api': 'blas',
  'internal_api': 'openblas',
  'prefix': 'libopenblas',
  'filepath': '/home/watanabe/github/simple_rbm/myenv/lib/python3.6/site-packages/numpy.libs/libopenblasp-r0-09e95953.3.13.so',
  'version': '0.3.13',
  'threading_layer': 'pthreads',
  'architecture': 'Zen',
  'num_threads': 32}]
```

Mac。

```txt
[{'user_api': 'blas',
  'internal_api': 'openblas',
  'num_threads': 10,
  'prefix': 'libopenblas',
  'filepath': '/Users/watanabe/github/simple_rbm/myenv/lib/python3.12/site-packages/numpy/.dylibs/libopenblas64_.0.dylib',
  'version': '0.3.23.dev',
  'threading_layer': 'pthreads',
  'architecture': 'Haswell'}]
```

OpenBLASのスレッド数設定は`OPENBLAS_NUM_THREADS`だそうな。なので、NumPyが裏で使うスレッド数を設定するには、

```py
OPENBLAS_NUM_THREADS=1 python3 hoge.py
```

などとすれば良い。`OMP_NUM_THREADS`じゃないのか・・・。

2024年度 理工学部 教授・准教授就任講演。僕はトップバッター。今回はちゃんとネクタイをした。

いかん、頭が全く回らん。
