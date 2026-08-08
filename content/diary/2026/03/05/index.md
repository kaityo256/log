---
title: "2026年3月5日"
date: 2026-03-05T00:00:00+09:00
lastmod: 2026-03-05T00:00:00+09:00
type: diary
source_month: "d202603.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

会議。

Vimハンズオン。テキストを少し修正したほうがいいなぁ。

研究室ミーティング。StarCraft IIの話。RTSのAIももう一度研究してみたい。

研究室飲み会の場所を予約した。条件をChatGPTに食わせて候補を出してもらって、URLに飛んで調べて予約。楽ちん。これは人生変わるな・・・

機械学習がらみ、すぐにバージョン不整合が起きるな・・・

TensorFlowのモデルをJSにエクスポートするやつ、うまく動かなかったので、えらく苦労して動くようにした。ついでにvenvではなくuvにしてみたら動かなくなった。原因不明。

で、時間切れで家に返ってvenvでやろうとしたらPythonが古いっぽい。pyenvで入れようとしたら古いバージョンしかない。pyenvも古かった。pyenvも入れ直し。

```sh
curl https://pyenv.run | bash
```

`.zshenv`に

```sh
export PYENV_ROOT=${HOME}/.pyenv
export PATH=${PYENV_ROOT}/bin:${PATH}
eval "$(pyenv init -)"
```

Python 3.11系を入れる。

```sh
pyenv install 3.11
pyenv global 3.11.15
```

これで学習、エクスポート、JS変換、HTMLからインポート全てできた。uvでやり直す元気はない。明日ここの講義ノート書いたら春の学校の準備おしまい。結構なエフォート持ってかれたな・・・
