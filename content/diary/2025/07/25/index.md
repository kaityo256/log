---
title: "2025年7月25日"
date: 2025-07-25T00:00:00+09:00
lastmod: 2025-07-25T00:00:00+09:00
type: diary
source_month: "d202507.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install Cython
python3 -m pip install nemo_toolkit['all']
```

```py
import numpy as np
np.int = int
np.float = float
np.str = str
import nemo.core
```

駄目だ。GitHubから行く。

```py
pip install --upgrade pip setuptools wheel
pip install Cython ninja
git clone https://github.com/NVIDIA/NeMo.git
cd NeMo
pip install -e .[all]
```

Pythonのバージョンが足りない。Kuguiにはcondaで入れたな。

```sh
$ python3 --version
Python 3.12.10
```

駄目だ。NeMoの要求するPythonのバージョン範囲が厳しい。3.12では駄目。3.11でも駄目。

```sh
conda install python=3.10
mkdir llama2-test
cd llama2-test
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install Cython ninja
pip install hydra-core omegaconf
pip install lightning
pip install braceexpand
pip install webdataset
pip install einops
pip install transformers
pip install sentencepiece
pip install h5py
pip install pandas
pip install matplotlib
pip install megatron
git clone https://github.com/NVIDIA/NeMo.git
cd NeMo
pip install .
```

```sh
git clone https://github.com/NVIDIA/Megatron-LM.git
cd Megatron-LM
pip install -e .
```

```sh
module load cuda/11.2
pip install torch
git clone https://github.com/NVIDIA/apex
pip install . --no-build-isolation
```

できたか？

```sh
$ ipython
import os
os.environ["NVIDIA_PYTORCH_VERSION"] = "24.03"
from nemo.core import ModelPT
model = ModelPT.restore_from("llama2-7b-nemo.nemo")
```

```sh
wget https://huggingface.co/pe-nlp/llama2-7b-nemo/resolve/main/llama2-7b-nemo.nemo
```

先にAPEXのインストールが必要か?

```sh
module load cuda/11.2 
python3 -m venv .venv
pip install --upgrade pip

pip install ninja
pip install packaging
git clone https://github.com/NVIDIA/apex
pip install torch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0
cd apex
APEX_CPP_EXT=1 APEX_CUDA_EXT=1 pip install -v --no-build-isolation .
```

駄目。物性研のCUDAが古い(11.2)のがまずいらしい。

Google Colabで試してみる？

```py
!pip install nemo_toolkit
!pip install hydra-core
!pip install lightning
!pip install braceexpand
!pip install webdataset
!pip install ijson
!pip install megatron megatron-core
!pip install sacrebleu
!pip install rouge_score
!pip install opencc
from nemo.collections.nlp.models.language_modeling import MegatronGPTModel
model = ModelPT.from_pretrained("pe-nlp/llama2-7b-nemo")
```

駄目だ。MegatronGPTModelが入らない。どうにもできない。
