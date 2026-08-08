---
title: "2023年9月22日"
date: 2023-09-22T00:00:00+09:00
lastmod: 2023-09-22T00:00:00+09:00
type: diary
source_month: "d202309.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

昨日のコード、もう少しスッキリ書けるなと思って修正。

```cpp
#include <cstdio>

int main(){
  const char *str[] = {"fizz", "buzz"};
  int a = 0, b = 0, c = 0;
  a = ++a + --a;
  b = --b + ++b + ++b;
  c = ++c + ++c + b;
  for (int i=1;i<16;i++){
    if (i%c==0){
      printf("%s\n",str[b]);
    }else{
      printf("%d\n",i);
    }
  }
}
```

前はif文が2つあってあまりきれいじゃなかったので整理した。

```cpp
  a = ++a + --a;
  b = --b + ++b + ++b;
  c = ++c + ++c + b;
```

このあたりに黒魔術感があって気に入っている。

[FizzBuzzをエンジニアの採用試験で出題したら半数が問題文を理解できなかったので公開します](https://komari.co.jp/blog/6936/)

結局、FizzBuzzができない人は、プログラミングができないのではなく、そもそも課題文を理解できていないのだ、という指摘。まぁそうだよね。

ChatGPT、本当にすごいな。SSHのデバッグログ見ても、どんなアルゴリズムが使われてるかわからなかったので食わせてみた。

ログを食わせる。

```txt
提供されたデバッグログは、SSH接続時にクライアントとサーバーがサポートする鍵交換(KEX)アルゴリズム、ホストキーのアルゴリズム、暗号化アルゴリズム、MAC、圧縮方法などのリストを示しています。しかしこのログから、実際に接続時に選択されたアルゴリズムは明確には分かりません。

実際に使われたアルゴリズムを知るためには、通常、デバッグログの続きを参照する必要があります。KEXのネゴシエーションが完了した後、選択されたアルゴリズムに関する情報がログに出力されます。その部分がこの提供されたログには含まれていないようです。

したがって、提供されたログの情報だけでは、実際に使われたアルゴリズムを特定することはできません。もし実際に使用されたアルゴリズムを知りたい場合、デバッグログの続きをチェックするか、再度`-vvv`オプション（より詳細なデバッグ情報を提供）を使ってSSH接続を試みると良いでしょう。
```

続きを食わせる。

```txt
デバッグログの続きを提供していただき、ありがとうございます。

以下の情報に基づいて、実際に使われたアルゴリズムを確認できます：

1. **鍵交換 (KEX) アルゴリズム**:
    ```
    debug1: kex: algorithm: curve25519-sha256
    ```
   これにより、`curve25519-sha256` が鍵交換アルゴリズムとして使用されたことがわかります。

2. **ホストキーのアルゴリズム**:
    ```
    debug1: kex: host key algorithm: ssh-ed25519
    ```
   これにより、`ssh-ed25519` がホストキーのアルゴリズムとして使用されたことがわかります。

3. **暗号化アルゴリズム**:
    - サーバーからクライアントへの暗号化:
    ```
    debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    ```
    これにより、`chacha20-poly1305@openssh.com` がサーバーからクライアントへの暗号化アルゴリズムとして使用されたことがわかります。

    - クライアントからサーバーへの暗号化:
    ```
    debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
    ```
    これにより、`chacha20-poly1305@openssh.com` がクライアントからサーバーへの暗号化アルゴリズムとして使用されたことがわかります。

4. **MAC (Message Authentication Code)**:
   両方の暗号化アルゴリズムのログに `<implicit>` と表示されているので、暗号化アルゴリズム自体が認証的な性質を持っているため、別途のMACが必要ないことを示しています。`chacha20-poly1305@openssh.com` は暗号化と同時にメッセージ認証も行うため、これが当てはまります。

5. **圧縮**:
    ```
    compression: none
    ```
   圧縮は使用されていないことがわかります。

以上の情報により、接続に使用されたアルゴリズムは以下の通りです：
- 鍵交換アルゴリズム: `curve25519-sha256`
- ホストキーのアルゴリズム: `ssh-ed25519`
- 暗号化アルゴリズム: `chacha20-poly1305@openssh.com`
- MAC: なし (暗号化アルゴリズムが認証も行うため)
- 圧縮: なし
```

いやだってさ、

```txt
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
```

という表示を見て`chacha20-poly1305@openssh.com`がアルゴリズム名だとはわからないでしょ。どこかに接続してんのかな、って思うじゃない。結局、chacha20がストリーム暗号、Poly1305がMACとのこと。
