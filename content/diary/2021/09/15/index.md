---
title: "2021年9月15日"
date: 2021-09-15T00:00:00+09:00
lastmod: 2021-09-15T00:00:00+09:00
type: diary
source_month: "d202109.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

断固今日中に座学を終わらせないと絶対にヤバい。

GitでfetchとpushのURLを変える。まず、リモート二つとローカル一つを作る

```sh
git init --bare test1.git
git init --bare test2.git
git init test
```

testでリモートを追加する。

```sh
cd test
git remote add origin ../test.git
```

fetchもpushも同じURLになる。

```sh
$ git remote -v
origin  ../test.git (fetch)
origin  ../test.git (push)
```

originという名前で、プッシュだけ別の場所にする。

```sh
git remote set-url --push origin ../test2.git
```

```sh
$ git remote -v
origin  ../test.git (fetch)
origin  ../test2.git (push)
```

同じ名前でfetchとpushが別のURLになった。

リモートを追加し、上流ブランチを設定せずにpush。

```sh
git push origin main
```

```sh
$ git branch -vva
* main                90bdb0e initial commit
  remotes/origin/main 90bdb0e initial commit

$ git status -b
ブランチ master
nothing to commit, working tree clean

$ git status -sb
## main
```

上流ブランチを設定してもう一度。

```sh
$ git branch -u origin/main
Branch 'main' set up to track remote branch 'main' from 'origin'.

$ git branch -vva
* main                90bdb0e [origin/main] initial commit
  remotes/origin/main 90bdb0e initial commit

$ git status -b
ブランチ main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

$ git status -sb
## main...origin/main
```

リベース後にpushするのに失敗する例。

```sh
git init --bare test.git
git init test
cd test
echo "Hello" > test.txt
git add test.txt
git commit -m "c1"
echo "Hello2" > test.txt
git commit -am "c2"
git branch feature
echo "Hello3" > test.txt
git commit -am "c3"
```

ここまででこんな歴史ができた。

```sh
$ git log --oneline
3f3255e (HEAD -> master) c3
8ac3073 (feature) c2
8269d34 c1
```

リモートを追加してpush。

```sh
git remote add origin ../test.git
git push -u origin master
```

```sh
$ git log --oneline
3f3255e (HEAD -> master, origin/master) c3
8ac3073 (feature) c2
8269d34 c1
```

featureブランチを伸ばす。

```sh
git switch feature
echo "test" > test2.txt
git add test2.txt
git commit -m "f1"
```

こうなった。

```sh
$ git switch master
$ git log --graph --all --oneline
* 7ade9dd (feature) f1
| * 3f3255e (HEAD -> master, origin/master) c3
|/
* 8ac3073 c2
* 8269d34 c1
```

masterからfeatureへrebaseする。

```sh
$ git rebase feature
First, rewinding head to replay your work on top of it...
Applying: c3

$ git log --graph --all --oneline
* adcc72b (HEAD -> master) c3
* 7ade9dd (feature) f1
| * 3f3255e (origin/master) c3
|/
* 8ac3073 c2
* 8269d34 c1
```

なんか変なことを言われたが、想定通りの歴史になった。この状態でpushを試みる。

```sh
$ git push
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to '../test.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

git mergeしたらgit pushできた。

```sh
$ git merge
$ git l
91a23b1 (HEAD -> master) Merge remote-tracking branch 'refs/remotes/origin/master'
adcc72b c3
7ade9dd (feature) f1
3f3255e (origin/master) c3
8ac3073 c2
8269d34 c1
$ git push
```

うーん、良い例にはならなかったな。

コミット済みの奴をgit commit --amendしてもpushできなくなるな。

```sh
git init --bare test.git
git init test
cd test
echo "Hello" > test.txt
git add test.txt
git commit -m "c1"
echo "Hello2" > test.txt
git commit -am "c2"
git remote add origin ../test.git
git push -u origin master
git commit --amend -m "c2'"
```

これで歴史が改変されて分岐する。git pushできなくなる。git mergeすれば歴史を共有できる。

```sh
git merge -m "merge"
git push
```

rebase版。

```sh
git init --bare test.git
git init test
cd test
echo "Hello" > test.txt
git add test.txt
git commit -m "c1"
git branch feature
echo "Hello2" > test.txt
git commit -am "c2"
git remote add origin ../test.git
git push -u origin master
git rebase -i feature
```
