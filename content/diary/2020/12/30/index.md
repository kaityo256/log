---
title: "2020年12月30日"
date: 2020-12-30T00:00:00+09:00
lastmod: 2020-12-30T00:00:00+09:00
type: diary
source_month: "d202012.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

学生さんのコードの動作がおかしいと言われて確認。多分できたと思う。

しかし、学生さんのコードがGitHubで管理されており、それにコラボレータとして招待してもらってclone、内容をチェックって、やってるところはやってるんだろうけど、なんかちゃんとしてて良くない？

Docker内で自分のリポジトリにコミットしてpushしたいが、Dockerイメージ内に認証情報を置きたくない場合、環境変数を使う方法がある。GIT_USERにユーザ名、GIT_TOKENにアクセストークン、GIT_REPOSITORYにリポジトリ(例えばkaityo256/log.git)を環境変数として入れておいて、

```sh
git push -u https://${GIT_USER}:${GIT_TOKEN}@github.com/${GIT_REPOSITORY}
```

とすればpushできる。以後、認証情報が残るのでgit pushだけで行ける。

ホスト側でこれらの環境変数を設定しておき、

```sh
docker run -e GIT_USER=${GIT_USER} -e GIT_TOKEN=${GIT_TOKEN} -it imagename
```

として渡してやればOK。面倒なので先のgit pushコマンドはgpとしてエイリアスしておいた。これでいろいろ捗るぞ・・・と。

Gmailがまた大事なメールをSPAMに。ダメだ。来年はもうforwardしよう。
