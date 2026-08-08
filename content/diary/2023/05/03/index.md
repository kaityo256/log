---
title: "2023年5月3日"
date: 2023-05-03T00:00:00+09:00
lastmod: 2023-05-03T00:00:00+09:00
type: diary
source_month: "d202305.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

前から入れようと思っていたGitHub CLIを導入。

[ここ](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)の指示通り。

```sh
type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg \
&& sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

```sh
$ gh --version
gh version 2.28.0 (2023-04-25)
https://github.com/cli/cli/releases/tag/v2.28.0
```

できた。ログインは後で。

前から書こうとしてた[二次方程式の話](https://zenn.dev/kaityo256/articles/quadratic_equation)を書いた。講義の余談で話したもの。
