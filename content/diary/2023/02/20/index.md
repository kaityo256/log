---
title: "2023年2月20日"
date: 2023-02-20T00:00:00+09:00
lastmod: 2023-02-20T00:00:00+09:00
type: diary
source_month: "d202302.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

MusikaをGoogle Colabで動かそうとすると、WAVファイルはできるのだが、`IPython.display.Audio`で読み込もうとするとランタイムが切断されてしまう。
SciPiでWAVを一度NumPy配列にすればOKだが、SciPyのreadだと左右2チャンネルが(length, 2)の形になるが、Audioで読み込ませるためには(2, length)でなければならないのでtransposeが必要。また、ファイル名が毎回変わるのにも対応しないといけない。

最終的にこうなった。

```py
import IPython
import numpy as np
from scipy.io.wavfile import read
import glob
!git clone https://github.com/marcoppasini/musika
%cd musika
!pip install -r requirements.txt
!python musika_generate.py --load_path checkpoints/techno --num_samples 1 --seconds 10 --save_path ./generate
file = glob.glob("/content/musika/generate/*.wav")[0]
rate, data = read(file)
IPython.display.Audio(data.transpose(), rate=rate)
```

Comp. Phys. Commun.に論文投稿準備する。RevTeXでいけそうな気もするが、公式はelsarticle.clsを推奨している。

[https://ctan.org/tex-archive/macros/latex/contrib/elsarticle](https://ctan.org/tex-archive/macros/latex/contrib/elsarticle)からzipをダウンロード。

```sh
cd build
wget http://mirrors.ctan.org/macros/latex/contrib/elsarticle.zip
unzip elsarticle.zip 
cd elsarticle  
latex elsarticle.ins
latexmk elsarticle-template-harv
```

insファイルのコンパイルによりclsファイルができる。とりあえずclsファイルとテンプレートtexだけでコンパイルできることを確認。GitHubに学生さん論文用のリポジトリを作成。もう少し中身を書いたら学生さんを招待する。
