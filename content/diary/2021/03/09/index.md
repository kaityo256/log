---
title: "2021年3月9日"
date: 2021-03-09T00:00:00+09:00
lastmod: 2021-03-09T00:00:00+09:00
type: diary
source_month: "d202103.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

免許の住所変更した。

マイナンバーカード4人分申請した。

論文を書こうとしたのだが、なんかWSL2でビルドできない。あと、texindentを入れようとしたら、tlmgrが古いとか言われる。

```sh
$ tlmgr update --self
(running on Debian, switching to user mode!)
tlmgr: Remote repository is newer than local (2017 < 2020)
Cross release updates are only supported with
  update-tlmgr-latest(.sh/.exe) --update
Please see https://tug.org/texlive/upgrade.html for details.
```

```sh
sudo apt update
sudo apt upgrade
```

でも、upgradableを見る限りTeXLiveは入っていない気がする？フルインストールしちゃえ。

```sh
sudo apt install texlive-full
```

Windowsだと死ぬほど時間かかるけど、WSL2だとどうだろう？

入った。これでlatexindentが入るかな？

```sh
$ latexindent --version
3.4.1, 2018-01-18
```

入ったみたい。

ダメだ。WindowsのWSL:UbuntuでVS CodeからLaTeX Buildしようとしてもどうしてもうまくいかない。実行マークが永遠にくるくる回るだけ。VS Codeのターミナルから開いて実行したらうまくいくのだが。

やむを得ず、VS Code保存時のビルドを切った。

```json
{
    "latex-workshop.latex.autoBuild.run": "never",
}
```
