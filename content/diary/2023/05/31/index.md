---
title: "2023年5月31日"
date: 2023-05-31T00:00:00+09:00
lastmod: 2023-05-31T00:00:00+09:00
type: diary
source_month: "d202305.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

5月が終わってしまうなぁ。

[Introducing the AI Research SuperCluster — Meta’s cutting-edge AI supercomputer for AI research](https://ai.facebook.com/blog/ai-rsc/) MetaのAI用スパコン。NVIDIAのDGX A100っぽい。インターコネクトはNVIDIA Quantumで、これはInfiniBand。なんでNVIDIA InfiniBandって言うのかと思ったら、いつのまにかMellanoxがNVIDIAに買収されてた。2020年か。SXMというのは接続方式。ずいぶん前からPCIeではなく、ソケット型でGPGPUが接続していたようだ。GPGPUの発展は全く追いかけてなかったから、最近の進展はさっぱりわからんな。

Markdownのスニペットとして、`align`って書いたら

```latex
$$
\begin{aligned}

\end{aligned}
$$
```

って出てきてカーソルが真ん中に移るやつ作ったんだけど、かなり便利だ。

メモ。

[COVID-19はポケモンが原因論文](https://www.the-scientist.com/critic-at-large/opinion-using-pokmon-to-detect-scientific-misinformation-68098)。

American Journal of Biomedical Science & Researchというジャーナルから「論文投稿して」というメールが届いたのだが、なんか見覚えあるなと思ったら「COVID-19はポケモンが原因論文」を掲載してしまったジャーナルですね。論文にわざわざ「この論文を出版する雑誌は査読を行っていないため、ハゲタカジャーナルであるに違いない」とか「この招待論文は査読を行っていない可能性が高い略奪的な雑誌に掲載されている」と書いてある論文が「査読」を通って掲載されたというもの。

配列と条件を渡して、「配列の要素すべてが条件を満たす時に`true`を返す関数`all`」と、「配列の要素のいずれか一つでも条件を満たす時に`true`を返す関数`any`」があったとする。この関数に空配列を入れた時、`all`と`any`を何を返すべきか。

僕は空集合に関しては全部真にして良いかな、と思ったが、多数派の意見は`all`は`true`、`any`は`false`を返すべき、というもの。

`all`は「集合の中に一つでも条件を満たさないものがあるか？」と読み替えるべき。すると空集合は条件を満たさないものを持たないから、`true`を返す。

`any`は、文字通り「集合の中に一つでも条件を満たすものがあるか？」を調べるべき。すると空集合は条件を満たすものを持たないから`false`を返す。PythonもRubyもそうなっている。

```py
all([])  #=> True
any([])  #=> False
```

```rb
[].all? #=> true
[].any? #=> false
```

へぇ、なるほどね。
