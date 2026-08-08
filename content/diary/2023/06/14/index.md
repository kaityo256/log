---
title: "2023年6月14日"
date: 2023-06-14T00:00:00+09:00
lastmod: 2023-06-14T00:00:00+09:00
type: diary
source_month: "d202306.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

夏季安全点検報告した。

ある数学的な概念について検索したら某質問回答サイトがひっかかったんだけど、内容がわりとヤバい気がする。初学者に、知識が怪しい中級者が答えている、みたいなイメージ。うーん。

あと、このサイト、「質問の体をとったマウンティング」が多くてびっくりする。「東大の数学の入試問題は、本当に数学がわかっている人が作っているのですか？」みたいな。いろいろすごい。

ウェブでのパスワードの変更、最初の「新しいパスワード」はコピペを許し、２つ目の「確認のためにもう一度入力してください」をコピペ不可にするの、意味がよくわからない。パスワードマネージャーを使っている場合、パスワードジェネレータを使って自動生成し、それをコピーして貼り付けるわけで、明らかに人間が記憶するより安全だし、一回目はコピペを許しているため、パスワードがクリップボードに入らないようにするみたいなセキュリティの意味もない(そもそもコピペしようとしてコピペ禁止に気づくので意味がない)。

懸案だった名刺発注済ませた。これまでコロナでほとんど人に会っておらず、名刺もほとんど消費してなかったのだが、最近は人に会うことが増えて名刺の減りが激しく尽きてしまった。

どうでも良いけど、「このメールはこれまで名刺を交換させていただいた方にお送りしております」という嘘をついて送ってくる営業メール、どうなのよ？ 僕が計測機器メーカーの人と名刺交換するわけないでしょ。

古いAMD EPYCマシンで`Python Setup.py egg_info" Failed with Error Code 1`というエラー。おそらくpipが古い。久しぶりにyum updateしたり。

```sh
wget https://bootstrap.pypa.io/pip/3.6/get-pip.py 
sudo python3 get-pip.py
```

sudoはよくないらしいが。

と思ったら、venvが通らなくなった。

```sh
$ python3 -m venv env
Error: Command '['/home/watanabe/temp/env/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.
```

とあるものを受け取る予定になっていたが、その配達が遅れ、慌てて取りに行くも鍵を忘れて居室に戻り、受け取ったことを別の人に連絡しなければならないのにそれを失念し、学生向けのアナウンスを作ったら日付が間違いだらけ。古いPCのエラーなんとかしようとしたらPython環境を破壊。今日はダメだ。

ハイブリッドミーティング用にビデオカメラをZoomにつなげる確認。ビデオのHDMI出力にコンバータ(IO DATAのGV-HUVC)をつなぎ、USBをPCにつなげるだけ。あとはZoom側でマイク、ビデオソースをIO DATAのGV-HUVCを選べばOK。簡単。USBとHDMI素晴らしい。規格考えた人えらい。

```sh
python3 -m venv myenv --without-pip  
source myenv/bin/activate 
wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
python3 get-pip.py
python3 -m pip install --upgrade pip
python3 -m pip install tensorflow Pillow
```
