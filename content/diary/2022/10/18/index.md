---
title: "2022年10月18日"
date: 2022-10-18T00:00:00+09:00
lastmod: 2022-10-18T00:00:00+09:00
type: diary
source_month: "d202210.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

QLEAPのセミナー。

プログラミング基礎同演習。ちょっと雑談が長かった。反省。

Stable diffusionを試す。楽しい。

研究室サーバにdocker-composeを入れる。なんｋな

```sh
wget https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-linux-x86_64
sudo cp docker-compose-linux-x86_64 /usr/local/bin/docker-compose
```

うまくいかない。dockerが古いっぽい。

```sh
sudo yum update
```

しまった、うっかりupdateしてしまった。Intelコンパイラのパスがまた壊れるかもしれない。

バックアップ代わりにメモ。

```sh
source /opt/intel/bin/compilervars.sh -arch intel64 -platform linux
PATH=/opt/openmpi/bin:$PATH
PATH=/opt/intel/compilers_and_libraries/linux/bin/intel64:$PATH
LD_LIBRARY_PATH=/opt/openmpi/lib:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/intel/compilers_and_libraries/linux/lib/intel64
MANPATH=/opt/openmpi/share/man:$MANPATH
export PATH LD_LIBRARY_PATH MANPATH
OMPI_MCA_btl_base_warn_component_unused=0
export OMPI_MCA_btl_base_warn_component_unused
```

大丈夫っぽい。

```sh
$ docker --version
Docker version 20.10.19, build d85ef84
```

```sh
cd stable-diffusion-webui-docker
docker-compose --profile download up --build
docker-compose --profile auto up --build
```

`docker-compuse up`に失敗して、エラーメッセージで検索したら、[自分のメモ](https://zenn.dev/kaityo256/scraps/c335ac8c76c5e1)がひっかかって解決。半年前の自分は現在の自分より賢いっぽい。

ローカルでやろう。

Macにdocker composeをインストール。

```sh
$ sudo curl -L https://github.com/docker/compose/releases/download/v2.11.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose    
```

```sh
git clone https://github.com/AbdBarho/stable-diffusion-webui-docker.git
cd stable-diffusion-webui-docker
docker-compose --profile download up --build
docker-compose --profile auto-cpu up --build
```

ダウンロードに時間かかるな。

GPUでやろうとしたらnvidia-mlのシェアードライブラリが見つからないとかいってきたので、`auto-cpu`で実行してみた。

```txt
exited with code 137
```

残念、うまく動かなかった。
