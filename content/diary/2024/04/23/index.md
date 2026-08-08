---
title: "2024年4月23日"
date: 2024-04-23T00:00:00+09:00
lastmod: 2024-04-23T00:00:00+09:00
type: diary
source_month: "d202404.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

Pythonでリアルタイムに2Dグラフィックを描画する方法を調べた(ChatGPTに聞いた)。いろいろあるが、Qtが良さそう。

PyQt6とPySide2というものがあるが、Google Trendsで調べたところ、PyQt6のほうがメジャーっぽいのでそれでいく。

```sh
mkdir pyqt_sample
cd pyqt_sample
source myenv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install pyqt6
```

まずは[ここ](https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/)にあるサンプルで線が引けることを確認した。Qtをほとんど使ったことがないので、アニメーションの方法がまだよくわからない。

mysqld(MariaDB)のメモリ消費をモニタしてから1日。順調に増え続けている。調べてみたら、MySQLのメモリリークはわりと問題になるらしい。`table_definition_cache`を小さくすれば良いかも、とのこと。

まず、ログイン名とパスワードは`wp-config.php`にDB_USER, DB_PASSWORDとして記述されている。このユーザ名とパスワードを使って、

```sh
mysql -u root -p 
```

としてログイン。`table_definition_cache`を表示。

```sql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1552
Server version: 5.5.68-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> SHOW VARIABLES LIKE 'table_definition_cache';
+------------------------+-------+
| Variable_name          | Value |
+------------------------+-------+
| table_definition_cache | 400   |
+------------------------+-------+
1 row in set (0.00 sec)

MariaDB [(none)]> exit
Bye
```

うーん、400と、あまり大きくなかった。

最悪、cronで毎週mysqldをリスタートとかかなぁ。アドホックだなぁ。もう少し様子見。

科研費の報告書(F-6-1とF-7-1)書いてオンラインで提出。

FSのSlackの立て替え払い、システムから出してみた。これで行けたら毎月で良いかな。

研究室Wikiの情報を整理した。もうGitHubのプライベートページに移行したい。

mysqldのメモリ消費、単調増加ではあるけど、現在5%弱で、1日で最大メモリの0.1%とかなので、1ヶ月のオーダーでメモリ不足になる可能性は低そう。編集とかで急増したり？謎。
