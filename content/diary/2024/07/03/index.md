---
title: "2024年7月3日"
date: 2024-07-03T00:00:00+09:00
lastmod: 2024-07-03T00:00:00+09:00
type: diary
source_month: "d202407.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

中間試験の答案用紙がOCR非対応だったため、OCR処理に失敗。

仕方なくtesseractを使ったOCRに挑戦・・・したが無理だった。

```sh
brew install tesseract
python3 -m venv myenv
source myenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install PyMuPDF Pillow pytesseract
```

さらにOpenCVも使う。

```sh
python3 -m pip install opencv-python-headless
```

駄目だった。結局手作業でOCR。すげー時間かかった。人間が一番低コスト・・・

せっかくあまり予定がない日だったのに、これで一日費やしてしまったなぁ。
