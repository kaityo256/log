---
title: "2022年9月19日"
date: 2022-09-19T00:00:00+09:00
lastmod: 2022-09-19T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

[自作OSで文字列をPC98に表示する](https://asanobuturi.github.io/document/2022/PC98APCOS/index.html)

すごい。また高校生が自作OSを作ってる。そして参考文献に川合さんの30日OS自作本。この本、多くの人の人生に影響を与えている。僕もこういう本が書きたい。30日並列MD本とか書きたい。

いやしかし、最近の高校生は部誌をMarkdownで集めてGitHubで公開するのか。時代だな・・・

RBMの学習の勉強。

* [Ankur Moitra（MIT）-制限付きボルツマンマシンの学習](https://www.youtube.com/watch?v=EpU7wZwoe9A)←よくわからなかった
* このHugo Larochelleさん(Université de Sherbrooke)の一連の講義が一番わかりやすいっぽい。
    * [Neural networks [5.4] : Restricted Boltzmann machine - contrastive divergence](https://www.youtube.com/watch?v=MD8qXWucJBY)
    * [Neural networks [5.5] : Restricted Boltzmann machine - contrastive divergence (parameter update)](https://www.youtube.com/watch?v=wMb7cads0go)
    * [上記の講義によるPython実装](https://github.com/dataplayer12/RBM)

ようやくKL距離と対数尤度関数が結びついた。忘れない内にまとめておく。

確率変数$\hat{X}$を考える。この確率変数はN種類の値をとり得るとする。$\hat{X} = i$となることを「事象$i$」と呼ぶ。ある事象$i$が起きる真の確率を$q_i$とし、それをモデルで再現したいとする。モデルパラメータが$\theta$の時に、そのモデルにおいて事象$i$が起きる確率を$p_i(\theta)$とする。真の分布とモデルによる分布のKL距離は

$$
\begin{aligned}
KL(\vec{q}|\vec{p}(\theta)) & \equiv \sum_i^N q_i \log \frac{q_i}{p_i} \\
&= \sum_i^N q_i \log q_i - \sum_i^N q_i \log p_i
\end{aligned}
$$

この距離をパラメータ$\theta$で微分するので、第一項は消え、第二項だけ考えれば良い。

さて、いま真の分布がわからない代わりに、$T$回事象を観測し、その$k$回目の事象が$S_k$であったとしよう。この時、尤度関数$l(\theta)$は

$$
l(\theta) = \prod_k^T P(\hat{X} = S_t | \theta)
$$

で表される。ただし$P(\hat{X} = S_t | \theta)$は、パラメータ$\theta$のもとで、確率変数が値$S_t$を取る確率である。後のために対数尤度にしておく。

$$
\log l(\theta) = \sum_t^T \log P(\hat{X} = S_t | \theta)
$$

さて、$T$回の試行のうち、事象$i$が起きた回数を$n_i$とする。すると、先程の尤度関数の和を試行に関する和から、事象の種類に関する和に書き直すことができる。

$$
\log l(\theta) = \sum_i^N n_i \log P(\hat{X} = i | \theta)
$$

$P(\hat{X} = i | \theta)$は、パラメータ$\theta$において事象$i$が起きる確率であるから$p_i$のことである。したがって、

$$
\log l(\theta) = \sum_i^N n_i \log p_i
$$

両辺を試行回数$T$で割ると、

$$
\frac{1}{T}\log l(\theta) = \sum_i^N \frac{n_i}{T} \log p_i
$$

$T$回の試行のうち、事象$i$が起きた回数が$n_i$なので、事象$i$が起きる確率$q_i$は$n_i/T$で近似できる。すると、

$$
\begin{aligned}
\frac{1}{T}\log l(\theta) &= \sum_i^N \frac{n_i}{T} \log p_i\\
&\sim \sum_i^N q_i \log p_i
\end{aligned}
$$

これは、KL距離の第二項にほかならない。
