---
title: "2023年9月6日"
date: 2023-09-06T00:00:00+09:00
lastmod: 2023-09-06T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

エクセルで「平成13年 6月」とか「令和 5年 3月」とか書かれている行を一気に西暦表示に変換する方法・・・をChatGPTに聞いてみた。

```vb
=IF(ISNUMBER(SEARCH("平成",C33)), 
    "19"&TEXT(VALUE(MID(C33,3,2))+88,"##")&"年 "&MID(C33,6,LEN(C33)-5), 
IF(ISNUMBER(SEARCH("令和",C33)), 
    "20"&TEXT(VALUE(MID(C33,3,2))+18,"##")&"年 "&MID(C33,6,LEN(C33)-5), 
    C33))
```

全然ダメじゃん。なんどかやりなおしてとりあえず平成はできた。

```vb
=IF(ISNUMBER(SEARCH("平成",C33)), TEXT(VALUE(MID(C33,3,2))+1988,"####")&"年"&MID(C33,6,LEN(C33)-5), C33)
```

令和にも対応させた。

```vb
=IF(ISNUMBER(SEARCH("平成",C33)), TEXT(VALUE(MID(C33,3,2))+1988,"####")&"年"&MID(C33,6,LEN(C33)-5), IF(ISNUMBER(SEARCH("令和",C33)), TEXT(VALUE(MID(C33,3,2))+2018,"####")&"年"&MID(C33,6,LEN(C33)-5), C33))
```

「令和元年」→「エラー」ムキー！！！！！

```vb
=IF(ISNUMBER(SEARCH("平成",C33)), TEXT(VALUE(MID(C33,3,2))+1988,"####")&"年"&MID(C33,6,LEN(C33)-5), IF(ISNUMBER(SEARCH("令和元年",C33)), "2019年"&MID(C33,7,LEN(C33)-6),IF(ISNUMBER(SEARCH("令和",C33)), TEXT(VALUE(MID(C33,3,2))+2018,"####")&"年"&MID(C33,6,LEN(C33)-5), C33)))
```

「令和元年7月」→「2019年月」ムキー！！！！

```vb
=IF(ISNUMBER(SEARCH("平成",C33)), 
    TEXT(VALUE(IF(MID(C33,3,1)="元",1,MID(C33,3,2)))+1988,"####")&"年"&MID(C33,IF(MID(C33,3,1)="元",5,6),LEN(C33)-IF(MID(C33,3,1)="元",4,5)), 
IF(ISNUMBER(SEARCH("令和",C33)), 
    TEXT(VALUE(IF(MID(C33,3,1)="元",1,MID(C33,3,2)))+2018,"####")&"年"&MID(C33,IF(MID(C33,3,1)="元",7,6),LEN(C33)-IF(MID(C33,3,1)="元",6,5)), 
    C33))
```

「令和元年7月」→「2019年」ムキー！！！！！！！！！！！！！！！！

今見てみると、いろいろ決め打ちでなんとかしようとしてドツボってる感じだな。自分で正規表現とかでスクリプト書いた方が早いな。

[GitHub演習の講義ノート](https://github.com/kaityo256/github)に「SSH認証」の項目を書き始めた。公開鍵による認証が何をやってるかわからない学生が多く、必要だと思ったので。
