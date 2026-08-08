---
title: "2023年1月5日"
date: 2023-01-05T00:00:00+09:00
lastmod: 2023-01-05T00:00:00+09:00
type: diary
source_month: "d202301.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Tensorflowをインストールしようとしたら、こんな警告が。

```txt
/home/username/.pyenv/versions/anaconda3-5.3.1/lib/python3.7/site-packages/tensorboard/compat/tensorflow_stub/dtypes.py:541: FutureWarning: Passing (type, 1) or '1type' as a synonym of type is deprecated; in a future version of numpy, it will be understood as (type, (1,)) / '(1,)type'.
  _np_qint8 = np.dtype([("qint8", np.int8, 1)])
```

これはNumPyのバージョンが合っていないのだそう。

```txt
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
tensorflow-cpu 2.2.0 requires scipy==1.4.1; python_version >= "3", but you have scipy 1.6.1 which is incompatible.
tensorflow-cpu 2.2.0 requires tensorboard<2.3.0,>=2.2.0, but you have tensorboard 1.13.1 which is incompatible.
tensorflow-cpu 2.2.0 requires tensorflow-estimator<2.3.0,>=2.2.0, but you have tensorflow-estimator 1.13.0 which is incompatible.
```

全体でなんとかすると事故りそうなので、仮想環境でなんとかする。

```sh
python3 -m venv tf
source tf/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow
```

だめだ。Pythonのバージョンがダメっぽい。

```sh
$ pyenv versions
  system
* anaconda3-5.3.1 (set by /home/watanabe/.pyenv/version)
```

anacondaが悪さしてるっぽいのでsystemに変える。

```sh
pyenv global system
$ python3 --version
Python 3.8.10
```

venvしようとしたら、python3-venvがないと言われ、入れようとしたらパッケージがたりないからapt-get update しろと言われる。
あらためて-m venvしようとしたらpipがないと言われる。

```sh
sudo apt-get update
sudo apt-get install python3.8-venv
sudo apt install pip
```

あらためてもう一回。

```sh
python3 -m venv tf
source tf/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow
python3 -m pip install matplotlib
```

できた。tensoflowをインストールする時に、必要なバージョンを指定してnumpyだのscipyだのインストールしてくれるから、これでOK。

いやしかし面倒だなぁ。

TensorFlow.kerasで、モデルを保存してから読み込むと、

```txt
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-0.kernel
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-0.bias
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-1.kernel
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-1.bias
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-2.kernel
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).layer_with_weights-2.bias
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.1
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.2
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.3
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.4
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.5
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.6
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.7
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.8
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.9
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.10
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.11
WARNING:tensorflow:Value in checkpoint could not be found in the restored object: (root).optimizer._variables.12
```

みたいなエラーが大量に出る問題、モデルの重みだけでなく、optimizerの状態を復元んしようとして失敗しているのが原因らしい。最適化を続けるのでなければモデルの重みだけで良いので、

```py
model.load_weights('filename').expect_partial()
```

と`expect_partial()`をつければOK。
