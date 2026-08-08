---
title: "2025年3月13日"
date: 2025-03-13T00:00:00+09:00
lastmod: 2025-03-13T00:00:00+09:00
type: diary
source_month: "d202503.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

秋月電子から[PICマイコン PIC12F508-I/P](https://akizukidenshi.com/catalog/g/g130195/)。懐かしい。PICだ。

[データシート](https://akizukidenshi.com/goodsaffix/pic12c5xx.pdf)を見ると、こんなに小さいのに非常に高機能であることがわかる。

大学時代、ロボコン部に所属していたが、PICの扱いを全く理解できなかったのを思い出す。中学・高校時代、アセンブリを全く理解できなかったのと同根であろう。そのあたりの思いは[OS自作にまつわる思い出話](https://zenn.dev/kaityo256/articles/jisakuos_adc2021)に書いた。

今調べたら、PICは一般名詞ではなく、マイクロチップ・テクノロジー社の製品の名前だそうだ。また、ずっと「Programmable Integrated Circuit」の略だと思ってたが、正しくは「Peripheral Interface Controller」の略だそうだ。知らなかった・・・。

昔はEPROMだったな。今はフラッシュROMらしい。

ロボコンつながりで、恐ろしく久しぶりに友人の日記を見つけた。2021年に再開したらしい。リンクは貼らないでおこう。まだ日記書いてたのね。人のこと言えないが。しかしこの友人、Wikipediaの記述がやたらと充実しているんだよなぁ。

自分の日記を読み返す。現在公開しているのは2018年11月からだが、2000年7月23日まで遡ることができる。一週間分まとめて「NOP」と書いたりしているが、それでもほぼ毎日書いてるのはすごい(自画自賛)。

ChatGPTに「2000年7月23日から今日まで何日間ですか？」と聞いたら、なんと8999日だそうな。マジで？ほぼ25年間なので25*365=9125だからそんなもんか。9000日分の日記。さすがにこれを全部AIに食わせたら「仮想俺」を作ることができそう。

明日は9000日目の日記か。ふむ。

学生時代、僕の公開日記を読んでいる人は多かった。今はここは誰も読んでいないはず。でも惰性で書き続けるのであろう。

RockeyにDockerをインストール。

```sh
sudo dnf config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo systemctl --now enable docker
```

Dockerインストール時にdockerグループが作られている。あとはこいつにグループパスワードを設定すればOK。

```sh
sudo gpasswd docker
```

```sh
$ docker ps
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.48/containers/json": dial unix /var/run/docker.sock: connect: permission denied
$ newgrp docker
Password: 
$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

通常では拒否られて、dockerグループに入ったら使える状態になった。
