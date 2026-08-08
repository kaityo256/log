---
title: "2021年8月19日"
date: 2021-08-19T00:00:00+09:00
lastmod: 2021-08-19T00:00:00+09:00
type: diary
source_month: "d202108.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

VSCodeのmarkdownlintの設定。インデントをスペース4つ分にする。

```json
    "markdownlint.config": {
        "MD007": {
            "indent": 4
        }
    }
```

なんか`.markdownlint.json`が効かなかったので、VSCodeに直接設定。

理科設備費は、Excelの一覧だけメール。後は紙で。

VSCodeのMarkdownのタブサイズ変更が効かなかったの、エディタが開いたファイルで自動的にタブサイズを認識していたからだった。

```json
    "[markdown]": {
        "editor.detectIndentation": false,
        "editor.tabSize": 4,
        "editor.insertSpaces": true,
        "editor.wordWrap": "on",
        "editor.quickSuggestions": false
    }
```
