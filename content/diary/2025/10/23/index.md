---
title: "2025年10月23日"
date: 2025-10-23T00:00:00+09:00
lastmod: 2025-10-23T00:00:00+09:00
type: diary
source_month: "d202510.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

なんか集中力が極めて低いなぁ。

読んでたなろう小説、よくある鈍感系主人公ハーレムものだったんだけど、主人公が一人に決めた上にIF系分岐もなくて驚いた。

最近、なろう小説で「はずれ」を引くことがおおくなり、前に好きだった小説を読み返したりしている。作業用BGMもAI系が増えてきており、今後は小説もAI生成のものを読むようになるんじゃなかろうか。自分の好みの設定、結末で、フレーバーだけ変えたものが大量に生成できるので、一生読み続けられるわけだ。うーむ。

WindowsにJavaをインストール。CrowdWalkではJDK 17でよいのだが、JDK 25を選んでみた。

[OracleのJava Downloadページ](https://www.oracle.com/jp/java/technologies/downloads/)へ。とりあえずx64 Installerを選択。

インストール後、Git Bashで見えるか見てみる。

```sh
$ java --version
java 25.0.1 2025-10-21 LTS
Java(TM) SE Runtime Environment (build 25.0.1+8-LTS-27)
Java HotSpot(TM) 64-Bit Server VM (build 25.0.1+8-LTS-27, mixed mode, sharing)

$ java --list-modules | grep javafx
```

Javaは入ったが、JavaFXは入ってないな。

[https://openjfx.io/](https://openjfx.io/)に行ってダウンロード。

ダウンロードした`openjfx-21.0.9_windows-x64_bin-sdk.zip`を展開して、出てきた`javafx-sdk-21.0.9`を`C:\Program Files\Java`に移動。

export PATH="C:\Program Files\Java\jdk-21\bin":$PATH
export CLASSPATH="C:\Program Files\Java\javafx-sdk-21.0.9\lib"
export JAVAFX_HOME="C:\Program Files\Java\javafx-sdk-21.0.9\lib"

```sh
$ export CLASSPATH=.
$ javac --module-path "C:\Program Files\Java\javafx-sdk-21.0.9\lib" --add-modules javafx.controls HelloFX.java
java --module-path "C:\Program Files\Java\javafx-sdk-21.0.9\lib" --add-modules javafx.controls HelloFX
```

これで実行できた。しかし、gradleが動かない。JDK25だと新しすぎるらしい。

25をアンインストールして、21をインストール。

```sh
export JAVA_HOME="C:\Program Files\Java\jdk-21"
./gradlew
```

できた。

CrowdWalk動いた！
