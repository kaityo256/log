---
title: "2025年10月17日"
date: 2025-10-17T00:00:00+09:00
lastmod: 2025-10-17T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

古いマシンのディスクが圧迫されたの、仮想ハードディスクのせいらしい。これ、ファイルを消すだけではだめで、論理的にファイルを消したあと、なんらかの方法で圧縮しないといけない。

マシンの設定続き。

Docker Desktopをインストール。

X11をインストール。

なんか最近のWSLは何もしないでもX11が飛ぶな。lab_startupを修正。

あと、何かするたびに「ポロロン」ってうるさいので無効化。

`~/.inputrc`を作成して以下を記述。

```sh
set bell-style none
```

端末再起動か、

```sh
bind -f ~/.inputrc
```

で反映。

CrowdWalkを生で実行してみる。

Macにインストール。JDKをbrewで入れてみる。

```sh
brew install openjdk@17
echo 'export PATH="/usr/local/opt/openjdk@17/bin:$PATH"' >> ~/.zshrc
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v17)' >> ~/.zshrc
```

```sh
$ java -version
openjdk version "17.0.16" 2025-07-15
OpenJDK Runtime Environment Homebrew (build 17.0.16+0)
OpenJDK 64-Bit Server VM Homebrew (build 17.0.16+0, mixed mode, sharing)
```

OK。

```sh
cd github
git clone https://github.com/crest-cassia/CrowdWalk.git
cd ~/CrowdWalk/crowdwalk
./gradlew
```

クラッシュした。Open JDKにはJavaFXがバンドルされていないかららしい。

```sh
brew uninstall openjdk@17
```

大人しくLiberica JDK 17 x86をインストールする。

```sh
brew tap bell-sw/liberica
brew install --cask liberica-jdk17-full
export JAVA_HOME="/Library/Java/JavaVirtualMachines/liberica-jdk-17-full.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
```

```sh
$ java --list-modules | grep javafx
javafx.base@17.0.16
javafx.controls@17.0.16
javafx.fxml@17.0.16
javafx.graphics@17.0.16
javafx.media@17.0.16
javafx.swing@17.0.16
javafx.web@17.0.16
```

できた。JavaFXが必要だったらしい。

Ubuntuの場合。

```sh
wget -q -O - https://download.bell-sw.com/pki/GPG-KEY-bellsoft | sudo apt-key add -
echo "deb [arch=amd64] https://apt.bell-sw.com/ stable main" | sudo tee /etc/apt/sources.list.d/bellsoft.list
sudo apt-get update
sudo apt-get install bellsoft-java17-full
export JAVA_HOME=/usr/lib/jvm/bellsoft-java17-full-amd64
export PATH=$JAVA_HOME/bin:$PATH
```

full版をインストールしないとJavaFXが含まれない。

だが動作しない。WSL経由ではOpenGLの3D表示がうまくいかないようだ。ネイティブじゃないと駄目か。

ヘッドセットが壊れたのでAmazon Businessで注文。

GitHub演習。K-LMSにあるパワーポイントのスライドのPDFが古かった。いろいろ直したつもりだったのだが、そこを直し忘れたか。

結局、DockerやWSLなどの仮想環境では無理っぽいな。
