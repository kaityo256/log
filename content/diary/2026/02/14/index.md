---
title: "2026年2月14日"
date: 2026-02-14T00:00:00+09:00
lastmod: 2026-02-14T00:00:00+09:00
type: diary
source_month: "d202602.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

昨日の続き。

lammpstrjファイルから温度を出力するようにしたが、標準出力に出しているとちょっと不便なのでファイルに保存するように修正。`fstream`をインクルードして、`LammpstrjAnalyzer`クラスに`std::ofstream ofs_;`を追加。コンストラクタでファイルを開く。

```cpp
#include <cstdio>
#include <lammpstrj/lammpstrj.hpp>
#include <string>
#include <fstream> // ここを追加

class LammpstrjAnalyzer{
private:
  const std::string filename_;
  int frame_;
  std::ofstream ofs_; //ここを追加

public:
  LammpstrjAnalyzer(const std::string filename): filename_(filename){
    frame_ = 0;
    ofs_.open("temperature.dat"); //ここを追加
  }

  void calc_temperature(const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms) {
    double e = 0.0;
    for (auto &a : atoms) {
      e += a.vx * a.vx + a.vy * a.vy + a.vz * a.vz;
    }
    e /= static_cast<double>(si->atoms);
    e /= 3.0;
    // 以下を修正
    ofs_ << frame_ * 500 << " " << e << std::endl;
    std::cerr << frame_ << std::endl;
    //printf("%d %f\n", frame_ * 500, e);
    frame_++;
  }

  void analyze(void){
    auto callback_function = [this](const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms){calc_temperature(si, atoms);};
    lammpstrj::for_each_frame(filename_, callback_function);
  }
};
```

標準エラー出力にフレーム番号を吐いておくと処理の進捗がわかって良い。実行すると`temperature.dat`が出力される。

```sh
$ make
$ ./lammpstrj-sample 
(LX, LY, LZ) = (20.000000, 20.000000, 20.000000)
N = 4000
0
1
2
3
4
5
6
7
8
9
10
$ cat temperature.dat
0 0.99975
500 1.03767
1000 1.03179
1500 1.0046
2000 0.953656
2500 0.925923
3000 0.903054
3500 0.861995
4000 0.833804
4500 0.821041
5000 0.806599
```

`.gitignore`に`*.dat`も追加しておく。

これで温度出力に関しては一段落。

次に、密度をVTKファイルとして出力する奴も作った。後でチュートリアルにまとめよう。

確定申告済ませた。
