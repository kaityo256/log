---
title: "2024年7月16日"
date: 2024-07-16T00:00:00+09:00
lastmod: 2024-07-16T00:00:00+09:00
type: diary
source_month: "d202407.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

数理物理、とりあえず微分形式まで書き終わった。

VSCodeのLaTeX WorkshopのLaTeXのインデントが大きすぎる(デフォルトで6?)。

Latex-workshop＞Latexindent: Argsの`-y=defaultIndent: '%INDENT%'`となっているところを、`-y=defaultIndent: '  '`にしたが、`\item`のインデントが6のままだなぁ。


```yaml
"latex-workshop.latexindent.args": [
        "-c",
        "%DIR%/",
        "%TMPFILE%",
        "-y=defaultIndent: '  '"
    ],
    "latex-workshop.docker.enabled": true
```

となっているのを、

```yaml
    "latex-workshop.latexindent.args": [
        "-c",
        "%DIR%/",
        "%TMPFILE%",
        "-l"
    ],
    "latex-workshop.docker.enabled": true
```

と`-l`スイッチを作り、

`localSettings.yaml`に

```yaml
defaultIndent: "  "
indentRules:
  item:
    lookFor: "\\item"
    children:
      default:
        indent: 2  # インデントのスペース数
```

と書いたら概ね希望通りのインデントになった。

VSCode上のLaTeXのビルドに失敗するように。なんかlatexmk:latest をdocker pullできないとかいってくる。原因はLatex-workshop＞Docker: EnabledがTrueになっていたから。これをオフにしたらローカルのlatexmkを使うようになった。

期末テストの解答ほぼ作った。解答欄まだ。
