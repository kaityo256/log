---
title: "2021年5月7日"
date: 2021-05-07T00:00:00+09:00
lastmod: 2021-05-07T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

本当は良くないらしいが、sudo pip3ですべてのユーザにインストール。

```sh
sudo yum install -y python3
sudo python3 -m pip install --upgrade pip
sudo /usr/local/bin/pip3 --no-warn-script-location install numpy pandas matplotlib h5py tensorflow
```

やっぱりメールに比べてSlackの方がコミュニケーションが圧倒的に早いよな。なにか聞いて、回答があった時、メールだと「○○です。回答をありがとうございます。この内容で○○させていただきます。どうぞよろしくお願いします」的なことを書くけど、Slackだとお辞儀マーク一個つけておしまい。

LinuxとRubyのデュアルコミッタがどのくらいレアか調べたい。Linuxのcontributerは2017年で15637人。RubyはGitHub上でのcontributerが336人。Rubyはすぐにリストを作れそうだが、Linuxは難しそうだなぁ。
