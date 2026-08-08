---
title: "2022年9月27日"
date: 2022-09-27T00:00:00+09:00
lastmod: 2022-09-27T00:00:00+09:00
type: diary
source_month: "d202209.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

今日やるべきことリスト

* プログラミング基礎同演習講義準備
* 物理情報工学ソフトウェア開発演習講義準備

プログラミング基礎同演習の課題をPDF化するスクリプトがエラー。

```sh
$ pandoc assignment.md -s -o assignment.pdf --highlight-style tango --latex-engine=lualatex -V documentclass=ltjarticle -V geometry:margin=1in -H ../mytemplate.tex
--latex-engine has been removed.  Use --pdf-engine instead.
Try pandoc --help for more information.
```

`--latex-engine`が消えている。`--pdf-engine`を使えとのことなので、Makefileを修正。そこだけ修正してなんとかなった。GitHubリポジトリのスライドが古かったので講義で使っているスライドに修正。

pptxからpdfにするのが鬱陶しかったので、スクリプトから変換できないか確認。

```sh
python3 -m venv myenv
python3 -m pip install --upgrade pip
python3 -m pip install aspose.slides
```

あー、今気づいたけど、仮想環境作ってるのにactivate忘れてる。そして、pipのアップグレード中に手作業でpptxからpdfへの変換作業が終わっている(ありがち)。

一応試してみる。

```py
import aspose.slides as slides

pptx = slides.Presentation("slide.pptx")
pptx.save("slide.pdf", slides.export.SaveFormat.PDF)
```

```sh
$ python3 conv.py
Traceback (most recent call last):
  File "conv.py", line 3, in <module>
    pptx = slides.Presentation("slide.pptx")
RuntimeError: Proxy error(PptxReadException): The type initializer for 'Gdip' threw an exception. ---> TypeInitializationException: The type initializer for 'Gdip' threw an exception. ---> DllNotFoundException: Unable to load shared library 'libgdiplus' or one of its dependencies. In order to help diagnose loading problems, consider setting the LD_DEBUG environment variable: liblibgdiplus: cannot open shared object file: No such file or directory
```

`libgdiplus`ってのが必要っぽい。入れてみる。

```sh
sudo apt-get update -y
sudo apt-get install -y libgdiplus
```

```sh
python3 conv.py
```

できた。・・・が「Evaluation only. Created with Aspose.Slides for .NETうんちゃら」という文章が追加される。なんやねん。あと、フォントがおかしくてダメ。おとなしくWindows側でRubyでwin32oleとか使った方がよさそう。

モジュールを全14回分作成。講義スライドを全てPDF化してアップロード。レポート課題をアップロード。レポートの締め切りを確認してレポートの提出先作成。出席確認クイズを作成。オンデマンド講義動画を確認して共有URLを作って貼り付け。TAの追加。ここまでやってから「公開」して、アナウンス。

なんというか、昔に比べて講義準備が大変になってない？講義ノートとスライドだけ教室に持っていけば良かったのが、今はめちゃくちゃやることがある気がする。

で、次は物理情報工学ソフトウェア開発演習か。
