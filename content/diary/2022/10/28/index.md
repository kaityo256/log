---
title: "2022年10月28日"
date: 2022-10-28T00:00:00+09:00
lastmod: 2022-10-28T00:00:00+09:00
type: diary
source_month: "d202210.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

アルゴ式、「標準入力 1-3」がおかしい。RubyだとACできない。

```rb
s = gets
puts(s*3)
```

で問題ないはず。Pythonではうまくいく。

```rb
s = gets.chomp
puts(s*3)
```

だと通った。なんかおかしい。改行コードの問題かな？

「標準入力 2-7」も同様。

```rb
s = gets.chomp
t = gets.chomp
if s==t
puts "Yes"
else
puts "No"
end
```

と、chompを入れないと通らない。

`p readlines`で見てみたら、`["turtle\n", "turtle"]`となっている。

```py
s = input()
t = input()
print(s.encode('utf-8').hex())
print(t.encode('utf-8').hex())
```

で食わせると、こっちは改行が入らない。

```rb
s = gets
t = gets
$stdout = $stderr
p s
p t
```

を食わせたら、

```txt
"turtle\n"
"turtle"
```

となる。うーん、これは意図する動作なんだろうか？これはバグじゃなくて、RubyのgetsとPythonのinputの違いなのか？

Pythonのinputは改行コードを削除するが、Rubyのgetsは改行コードを削除しない？

Vimがファイル保存時に自動で最後に改行を入れるので気づかなかった。これ、前もハマったような。

懇親会の会場予約した。貸し切りにできてよかった。

GitHub演習。ミスがいくつかあったので修正しないと。→修正した。

GitHub演習の来週分、大幅な変更があったので直してスライドと課題をK-LMSにアップロードした。
