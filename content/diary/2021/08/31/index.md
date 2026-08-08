---
title: "2021年8月31日"
date: 2021-08-31T00:00:00+09:00
lastmod: 2021-08-31T00:00:00+09:00
type: diary
source_month: "d202108.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

何？もう8月終わりなの？

ながらくsvnを使っていたので、どうしてもci, stといったコマンドを使いたがっていたが、ちゃんとcommit、statusを入力するようにした。さらに、checkoutのかわりにswitchを使うように練習中。学生さんに変な癖つけるわけにはいかないしね。

Git 内部探訪。git init 直後は、.git/HEADは`

```sh
ref: refs/heads/main
```

とmain(master)ブランチを指している。しかし、init直後は`.git/refs/heads`は空っぽ。この状態で`git log`を叩くと、

```sh
$ git log 
fatal: your current branch 'main' does not have any commits yet
```

つまり、「HEADが指すブランチが存在しなければ、コミットが無い」と判断する。また、この時点ではindexも存在しない。

`git add`するとindexが作られる。

`git commit`してはじめて`.git/refs/heads/main`が作成される。

さて、`git log`が「歴史があるかどうか」は「対応するブランチに対応するファイルがあるかどうか」で判断しているので、それを削除すれば歴史が無いと判断する。

```sh
git switch -c hoge
```

これで`.git/refs/heads/hoge`が作られ、`.git/HEAD`がそこを指す。

ここで、`hoge`ブランチファイルの名前を変えてしまおう。

```sh
mv .git/refs/heads/hoge .git/refs/heads/hoge.org 
```

これで、HEADは`.git/refs/heads/hoge`を指しているが、そのファイルは存在しない、という状態になった。この状態で`git log`を叩くと、

```sh
$ git log
fatal: your current branch 'hoge' does not have any commits yet
```

と「歴史が無いよ」と言われる。しかし、`.git/index`は存在するので、`git diff`は使える。

```sh
$ echo "hogehoge" >> hello.txt
$ git diff
diff --git a/hello.txt b/hello.txt
index e965047..0e05194 100644
--- a/hello.txt
+++ b/hello.txt
@@ -1 +1,2 @@
 Hello
+hogehoge
```

indexも消してしまおう。

```sh
rm .git/index
```

これは`git init`直後の状態となるので、`git diff`が何も表示しなくなり、`git status`が`hello.txt`をUntracked filesと認識する。

```sh
$ git diff
$ git status
On branch hoge

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    hello.txt

nothing added to commit but untracked files present (use "git add" to track)
```

なるほどね。
