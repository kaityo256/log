---
title: "2021年9月2日"
date: 2021-09-02T00:00:00+09:00
lastmod: 2021-09-02T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Windowsのプリンター関連の「モニタリングツール」というのが入っているのだが、それがアップデートを要求してきた。何の気なしに「更新履歴」を見てみたら「社名変更」だけでずっこけてしまった。

なんかBoxeditというアプリが常駐してて何かと思ったら、Box上のファイルをローカルで開くためのツールらしい。要するにローカルにダウンロードしたファイルを監視し、変更があったら裏でアップロードするツール。うーむ。

[C++ AMPの死について](https://zenn.dev/wx257osn2/articles/rip_cxx_amp-ksaudhawigubweinfwklaeiuhfawelifh)

なんか、Intelの奴も死んでなかったっけ？

思い出した、[Intel Cilk Plus](https://www.isus.jp/products/c-compilers/goodbye-cilk-plus-01/)だ。

研究室ミーティング。本読み輪講。一冊終わりそう。素晴らしい。

Gitのハッシュがどうしても合わないと悩んでいたら、Vimが保存時に行末に改行コードを自動的に付与するという仕様のせいだった。しらなかった。

Pro Gitのハッシュ値の計算をする例をPythonで書き直す。

```py
import hashlib
content = "what is up, doc?"
store = f"blob {len(content)}\0{content}".encode("utf-8")
hash = hashlib.sha1(store).hexdigest()
print(hash) #=> bd9dbf5aae1a3862dd1526723246b20206e5fc37    
```

できた。続き。

```py
import zlib
data = zlib.compress(store)
print(bytes.hex(data)) #=> 789c4bcac94f5230346328cf482c51c82c56282dd05148c94fb607005f1c079d
```

こっちもできた。gitの作るオブジェクトと比べる。

```sh
git init
echo -n "what is up, doc?" > test.txt
git add test.txt 
```

この時点で「bd9dbf5aae1a3862dd1526723246b20206e5fc37」というオブジェクトができて、中身が「789c4bcac94f5230346328cf482c51c82c56282dd05148c94fb607005f1c079d」になっているはず。

```sh
$ od -tx1 .git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 
0000000    78  01  4b  ca  c9  4f  52  30  34  63  28  cf  48  2c  51  c8
0000020    2c  56  28  2d  d0  51  48  c9  4f  b6  07  00  5f  1c  07  9d
0000040
```

なってますね。

もう一度、`Hello Git!"でやりなおす。

ハッシュ値が一致することを確認。

```sh
$ echo -n 'Hello Git!' > test.txt
$ git hash-object test.txt 
fdc3d3cd37c23aeb665aa995f395d9c6979bd508

$ { echo -n 'blob 10\0';cat test.txt} | shasum 
fdc3d3cd37c23aeb665aa995f395d9c6979bd508  -
```

中身が一致することを確認。

```sh
$ git init
$ git add test.txt
$ od -tx1 .git/objects/fd/c3d3cd37c23aeb665aa995f395d9c6979bd508
0000000    78  01  4b  ca  c9  4f  52  30  34  60  f0  48  cd  c9  c9  57
0000020    70  cf  2c  51  04  00  34  98  05  7a                        
0000032
```

```py
import zlib
content = "Hello Git!"
store = f"blob {len(content)}\0{content}".encode("utf-8")
data = zlib.compress(store)
print(bytes.hex(data))
```

```sh
$ python3 test.py
789c4bcac94f52303460f048cdc9c95770cf2c5104003498057a
```

一致していますね。めでたい。これでGit内部についてはおしまいかな。

Gitのblobは`binary large object`の略らしい。ほんとか？

少なくとも[GitHubはそう言っている](https://docs.github.com/en/rest/reference/git#blobs)と。

Gitのコミットオブジェクトは

* スナップショット全体を保存するtreeオブジェクト
* 親コミット
* 著者やメールアドレス
* コミットメッセージ

を含んでいる。

スナップショットを保存するtreeオブジェクトは、ワーキングツリーのファイルとディレクトリを保存している。ディレクトリはtree、ファイルはblobオブジェクトとして保存。blobオブジェクトはファイル名を保存しておらず、blobとファイル名を結びつけるのはtree。したがって、同じ内容で異なるファイル名を持つファイルがワーキングツリーにある場合、blobオブジェクトは一つになり、treeオブジェクトが二つのファイルとして認識する。

よし、Gitの内部状態についてはもうだいたい理解したな。
