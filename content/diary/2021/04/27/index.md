---
title: "2021年4月27日"
date: 2021-04-27T00:00:00+09:00
lastmod: 2021-04-27T00:00:00+09:00
type: diary
source_month: "d202104.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

ffmpeg、なんか思ったよりスレッド使ってるな。

```sh
ffmpeg -i aiyoshi02.mp4 -threads 32 -crf 24 aiyoshi02_low.mp4  5570.32s user 132.12s system 1230% cpu 7:43.29 total
```

CPUは12コアちょっとしか使っていないのに、

```sh
$ cat /proc/$(pgrep ffmpeg)/status | grep Threads
Threads: 116
```

使っているのは116スレッド、マジか。

mediainfoをCentOSに入れる。

```sh
sudo yum --enablerepo extras install epel-release 
sudo yum install -y mediainfo-gui mediainfo libmediainfo   
```

mediainfoでHTML形式で出力すると、スレッド数が見える。

```txt
threads=32 / lookahead_threads=4 / sliced_threads=0
```

ふむ、わからん。

実験。

package-lock.json、消してはいけないらしい。npm installで作り直せるらしい。

```sh
git merge origin/main       # ここでpackage-lock.jsonがconflict
npm install zenn-cli@latest # package-lock.jsonを作り直す
git add package-lock.json
git commit -m "updates package-lock.json"
```

今の所これで問題はおきてない。

* [package-lock.jsonについて知りたくても聞けなかったこと](https://qiita.com/fj_yohei/items/7ca887a45e0855917279)

何が起きたかわかったぞ。

* 二箇所でzenn-contentを作った
* あるところでzenn-cliのupdateをした (package-lock.jsonが更新)
* 別のところでgit fetch;mergeしようとしたら package-lock.jsonがconflict
* mergeしようとした場所で `npm install zenn-cli@latest`でpackage-lock.jsonを作り直せば良い
