---
title: "2024年5月27日"
date: 2024-05-27T00:00:00+09:00
lastmod: 2024-05-27T00:00:00+09:00
type: diary
source_month: "d202405.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

シミュレーション工学、今学期の最後。なんか今回は時間配分が下手だった気がするなぁ。

しばらくRuby触ってなかったからかなり忘れてる。rbenvも完全に忘れてる。

```sh
brew update
brew upgrade ruby-build
rbenv install 3.3.1
rbenv local 3.3.1 
gem install ruby-lsp
gem install rubocop
```

そしてVSCodeにRuby LSP拡張を入れる。settings.jsonに

```json
    "rubyLsp.formatter": "rubocop",
    "[ruby]": {
        "editor.formatOnSave": true
    }
```

を追加。FormatOnSaveがワンテンポ遅れるのが気になる。

Slackの立て替え払い出した。
