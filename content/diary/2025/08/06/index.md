---
title: "2025年8月6日"
date: 2025-08-06T00:00:00+09:00
lastmod: 2025-08-06T00:00:00+09:00
type: diary
source_month: "d202508.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Docker + CrowdWalkを試してみる。

```sh
export LANG=ja_JP.UTF-8
export JAVA_OPTS='-Dgroovy.source.encoding=UTF-8 -Dfile.encoding=UTF-8'
git clone https://github.com/crest-cassia/CrowdWalk.git
cd ~/CrowdWalk/crowdwalk
./gradlew
```

```sh
docker build -t crowdwalk-docker .
```

Ubuntuにxeyesをインストール。

```sh
sudo apt install -y x11-apps
```

```sh
xhost + localhost
docker run --rm -e DISPLAY=host.docker.internal:0 crowdwalk-docker
```

これでうまくいった。

Rockeyにxclockをインストール。

```sh
sudo dnf install -y xclock
```

サーバ側で`/etc/ssh/sshd_config`で以下を設定してからsshd再起動。

```sh
X11Forwarding yes
X11UseLocalhost yes 
```

```sh
sudo systemctl restart sshd
```

xauthをインストール。

```sh
sudo dnf install -y xauth
```

xclockで動作確認。

```sh
xclock
```

OK。

Rockeyにxauthをインストール。

```sh
sudo dnf install xorg-x11-server-utils
```

駄目だ。どうしてもSSH+Docker+X11ができない。後回し。
