---
title: "2021年5月12日"
date: 2021-05-12T00:00:00+09:00
lastmod: 2021-05-12T00:00:00+09:00
type: diary
source_month: "d202105.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物理情報工学特別講義の接続テストした。事前テストしてよかった。

というわけで車輪の再開発記事[ZshでプロンプトにGitリポジトリの情報を表示する](https://zenn.dev/kaityo256/articles/zsh-vcs-prompt)を公開したら、[Powerlevel10k](https://github.com/romkatv/powerlevel10k)というのを教えていただいた。なんかプロンプトがかっちょいい。

こういう自作系記事を書いた時、「○○使わないの？」みたいな揶揄をする人が結構いてアレなんだけど、こういう「自作も良いけどこれもおすすめです」みたいなコメントはうれしいなぁ。

```sh
brew install make imagemagick
```

```sh
sudo apt-get update
sudo apt install -y make build-essential imagemagick
sudo apt-get install python3-pip
```

```sh
python3 -m pip install --upgrade pip
python3 -m pip install numpy matplotlib
```

上記あたり、lab_startupに入れないとな。

だめだ。うちのWSL2のUbuntuでimagemagickがインストールできず、404になる。おそらく18.04から20.04にアップグレードしたせいだ。

いろいろやったが、最終的にキャッシュを消したらうまくいった。

```sh
cd /var/lib/apt
sudo mv lists lists.org
sudo apt-update
```

やれやれだ。

次、WSL2でJupyter Notebook。

```sh
sudo apt install -y jupyter-notebook
```

WSL2の時間がまたずれた。

```sh
sudo hwclock -s
```

でなおった。.zshrcに入れるべきか。

Powerlevel10k、試してみたが、残念ながらデフォルトではSubversionに対応していないようだ。p9kの機能は使えるとのこと。とりあえず使うのは見送り。使うには以下を.zshrcに入れること。

```sh
source ~/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
```

lab_startupのPython設定書いた。28日漬け込んだissueを閉じたぞ。

実験のレポートを採点した。
