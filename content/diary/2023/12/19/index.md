---
title: "2023年12月19日"
date: 2023-12-19T00:00:00+09:00
lastmod: 2023-12-19T00:00:00+09:00
type: diary
source_month: "d202312.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

1on1 x 3。

プログラミング基礎同演習。「Pythonはどう動くのか」。

GitHubのメインブランチの変更、いつもメニューがわからなくなる。Default branchの設定は「General」にあるんだよね。いつも「Branches」を探しに行って「あれ？ないな。Protection Rulesを設定しないとメインブランチ設定できないのかな？」って思っちゃう。

今年5月18日に開けたissueを閉じた。エラい。

[メモ：PyTorchの歴史](https://twitter.com/soumithchintala/status/1736555740448362890)

機械翻訳版を下につけておく。

PyTorch の設計の起源、Lua との関係、JAX との絡み合った深い関係、Chainer との共生関係

PyTorch の基礎作りは、もともと 2016 年の初めに、Torch7 の貢献者らの間でオンラインで始まりました。

* Torch7 (~2010-2017)
    * 最近では、Lua 経由で使用されていたため、Torch7 を一般に LuaTorch とも呼びます。トーチ 7 は、2010 年に Ronan Collobert @clmt と @koraykv によって書かれました。私は 2012 年から正式な「メンテナー」の立場で Torch7 に深く関与し、2014 年 4 月にこれら 3 人の原作者に加わりました。 
* Refactoring LuaTorch to be language agonstic (late 2015 to mid 2016)
    * 線形代数とニューラル ネットワーク用のすべての CPU と CUDA コードを備えた LuaTorch の C バックエンドは、Lua と深く結びついていました。そこで、 @lantiga, @neurosp1ke, @szagoruyko5, 私, @apaszke, @fvsmassaを中心とした多くのメンバーが、これらのバックエンドを Lua に依存せず、独立して使用できるようにリファクタリングしました。私たちは、LuaTorch を新しいモダンなデザインに移行する必要があるとオンラインで議論した後にこれを実行しましたが、そのデザインがどのようなものであるべきかを完全に枠組みしていませんでした。
* Writing a new Python based Torch (mid 2016)
 2016 年の初めにインターンシップを探して私に連絡をくれました。当時、@AIatMeta の LuaTorch チームは全体で約 3 人 (@GregoryChanan, @TrevorKilleen と私) でした。私は Adam に、モダンなデザインの LuaTorch の次のバージョンを構築するためのインターンシップに来てくれるように頼みました。 @colesbury はプロジェクトの合間だったので、彼もフルタイムで参加しました。私たちは、特に次の 2 つの目的のために、LuaTorch、LuaTorch-nn コードベースのフォークから開始しました。
  1. TH/THC および THNN/THCUNN C バックエンド
  2. LuaTorch のチェックポイントとの互換性を構築し、LuaTorch ユーザーがスムーズに PyTorch を継続できるようにします。これは、LuaTorch の「nn」コードを Python にトランスパイルすることで実現しました。 PyTorch ではこのパッケージを「torch.legacy.nn」と呼びました。
  それから、デザイン自体についても、私たちはたくさんのデザインについて議論しました。強いインスピレーションは次のとおりです。
  1. torch-autograd (@awiltschko および @clmt によって作成されました)
  2. Chainer ( @PreferredNetのチームによって作成されました)。@ebetica Chainer が大好きで、これが最高だと熱心に話してくれたので、一緒にこれを作るために参加してくれました。ナタリア・ギメルシェインやパートタイム @adamlerer など、他にもかなりの数の人々がさまざまな方法で関与しました。私たちは PyTorch の新しい設計のコードを最初から書きました。
* The connection to JAX: inspiration of HIPS/autograd
    * @awiltschko の torch-autograd (これは PyTorch の設計に大きなインスピレーションを与えました) は、@SingularMattrix, @DougalMaclaurin, @DavidDuvenaud と @ryan_p_adams,の HIPS/autograd ライブラリから直接インスピレーションを得たもので、その間接的な意味では、Ryan のライブラリから強いインスピレーションを受けました。実際、私たちは特定の起源についてあまりにも無頓着だったので、Autodiff エンジンに「torch.autograd」という名前を付けました。これは、autodiff コミュニティ内では物事を「autograd」と呼ぶのが標準であると考えたためです。その後、私たちのサブパッケージの名前が彼らの「autograd」パッケージと競合していることについて、@SingularMattrixとチームに謝罪しなければなりませんでした。その後、 @SingularMattrix @DougalMaclaurin らは JAX を作成し、HIPS/autograd の設計の探求を続けました。
* The inspiration from Chainer -> PyTorch and the inspiration for PyTorch -> Chainer v2
    * Chainer は強いインスピレーションを与えてくれました。私たちは Chains などのコンセプトがとても気に入りました。 Chainer の開発者は私たちの友人であり、彼らともよく交流しました。私は2017年に彼らを日本に訪ねました。私の意見では、Chainer のデザインは革新的なデザイン--で、当時としては非常に独創的で、かなり素晴らしいものです。私たちはそこからインスピレーションを得たことを誇りに思います。ただし、一般に誤解されたり誤って帰属されたりするのとは異なり、私たちは Chainer の設計をそのまま複製しただけではありません。人々は、PyTorch の設計が Chainer の設計とまったく同じであるため、その起源が単なるコピーアンドペースト--であり、それは共進化を理解していないためであるとオンラインに投稿しています。 PyTorch のリリース後、Chainer は PyTorch の優れたアイデアの一部を組み込むように進化し、最終的には同じように見えるように統合されました。たとえば、Chainer の nn Chains では、すべてのモジュールをコンストラクターに渡す (または add_link を使用する) 必要がありました。自己代入の概念 (ie) `self.conv = nn.Conv2d (...)` 、`Parameter` の概念は、Chainer v1 からの進化したアップグレードとして導入したものです。また、インプレース操作で正確性の問題を検出するための「変数バージョニング」など、autodiff エンジンの実装方法--を革新的に変更しました。また、その他のいくつかの新しいアイデア、最終的に v2 の Chainer に戻されたアイデアなども革新的に変更しました。Chainer のコミュニティが開発を停止したいと考えたとき、 @PreferredNet友好的かつ積極的に PyTorch コミュニティに参加しました (参考文献のリンク)。
* Post-launch evolution (2017 to present)
    * この投稿には PyTorch について説明するスペースがありません。
        * Caffe2 からのアイデアを追加する進化 (@jiayq @dzhulgako et. al)
        * 素晴らしいと思われるものにたどり着くまでの 5 つのコンパイラ設計 (Zach DeVito、 @ezyang @apaszke @jamesr66 Jason Ansel、Christian Sarofeen 他)
        * JAX と functorch の設計からのインスピレーション (Richard Zou、@cHHillee @vfdev_5 Animesh Jain)
        * 私たちの分散型設計と進化全体
        * スパースパッケージの起源 (@braizh) とその進化 ( @cpuhrsch et. al.)
        * PyTorch のドメイン ライブラリ
        * データロード (@colesbury @TongzhouWang )
        * コミュニティのデザイン、コミュニティの成長、インセンティブのデザインの革新 ( @ptrblck_de Alban Desmaison、私)
        * GPU コードにおけるいくつかの革新 (NVIDIA および Meta の主要人物数名)
  私が含めなかった PyTorch の他の多くの部分--は、この時点である程度モノリスになっています。

アイデアの帰属を明らかにすることは健全で素晴らしいことなので、もっと頻繁に行うべきです
PyTorch がリリースされて以来、いくつかの新しいライブラリが PyTorch の設計とアイデアを使用しています--私たちが導入した特定の新しいアイデアは、最終的には他の多くのライブラリに伝わりました-- 。これは素晴らしいことです。
私たちは、これまでの仕事からインスピレーションを得てきたことを誇りに思いますし、その後の仕事にもインスピレーションを与えてきたことを誇りに思っています。
また、私たちは-- torch-autograd、chainer、その他、より小さな方法で私たちにインスピレーションを与えてくれた多くのプロジェクトからインスピレーションを得たことを常に明確に示していることに誇りを持っています --。
私は、人々はこれを十分に行っておらず、自分の起源を明確に帰属させていない--と思います（p36）歴史を消去するためにエゴまたは企業の統制が機能するようになり-- 、人々はここでもっと行動する必要があります。その意味で、フレームワーク設計を科学的な取り組みとして捉え、アイデアや進化についてオープンに議論し、その起源やインスピレーションを誇らしげに語る JAX の友人たちを私は本当に誇りに思います。

参考文献:

1. My reply in March'17 on the origins of PyTorch: <https://discuss.pytorch.org/t/pytorch-tutorial-for-deep-learning-researchers/1001/3?u=smth>
2. Chainer's v1 design: <https://github.com/chainer/chainer/blob/v1/examples/imagenet/googlenet.py#L11-L33>
3. <https://pytorch.org/blog/pytorch-adds-new-tools-and-libraries-welcomes-preferred-networks-to-its-community/>
4. PyTorch's autodiff innovations in a short paper: <https://openreview.net/pdf?id=BJJsrmfCZ>
5. The PyTorch paper: <https://proceedings.neurips.cc/paper_files/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf>

GitHubの開いてるIssue一覧、結局検索で「author:kaityo256 state:open type:issue」で探せってことか。確かにそれで普通に見つかるからいいのか。
