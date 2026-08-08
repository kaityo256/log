---
title: "2026年2月13日"
date: 2026-02-13T00:00:00+09:00
lastmod: 2026-02-13T00:00:00+09:00
type: diary
source_month: "d202602.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

卒論と修論を製本に出した。こういうのが研究室に溜まっていくとうれしいですね。

輪講用の本を注文。

```txt
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
```

マジか。もう耐量子アルゴリズムの時代なのか。

サーバを更新しないといけない。まずはWordpressのwp-contentのバックアップのためにrsyncを走らせる。rsyncはいつも最後の「/」がどっちかわからなくなるので、Makefileに残しておく。後でDockerでなんとかする。

lammpstrj-parserのテスト。

```sh
mkdir lammpstrj-parser-sample
cd lammpstrj-parser-sample
git init .
git submodule add https://github.com/kaityo256/lammpstrj-parser external/lammpstrj-parser
```

`main.cpp`を作成。

```cpp
#include <lammpstrj/lammpstrj.hpp>

int main() {
}
```

`Makefile`を作成。

```makefile
CXX = g++
CXXFLAGS = -std=c++14 -O2 -Iexternal/lammpstrj-parser/include

all: lammpstrj-sample

lammpstrj-sample: main.cpp
  $(CXX) $(CXXFLAGS) main.cpp -o $@

.PHONY: clean

clean:
  rm -f lammpstrj-sample
```

`make`できることを確認。

```sh
$ make 
g++ -std=c++14 -O2 -Iexternal/lammpstrj-parser/include main.cpp -o lammpstrj-sample
```

うまくいっていたら、以下の内容の`.gitignore`を追加。

```txt
lammpstrj-sample
*.lammpstrj
log.lammps
```

後のためにlammpsの出力ファイルも追加しておく。

ここまでで以下のような表示になるはず。

```sh
$ git status -s 
A  .gitmodules
A  external/lammpstrj-parser
?? .gitignore
?? Makefile
?? main.cpp
```

これらを全て追加してコミットする。

```sh
git add .
git commit -am ":tada: initial commit"
```

相分離シミュレーションを実施。以下のようなインプットファイルを`test.input`として作成。

```txt
units       lj
atom_style  atomic
boundary p p p
timestep 0.001

variable rho equal 0.5
variable L equal 10.0

lattice fcc ${rho}
region box block 0 ${L} 0 ${L} 0 ${L}
create_box 2 box
create_atoms 1 box
set type 1 type/fraction 2 0.5 98765

mass 1 1.0
mass 2 1.0

pair_style lj/cut 2.5
pair_coeff 1 1 1.0 1.0 2.5
pair_coeff 1 2 1.0 1.0 1.12246
pair_coeff 2 2 1.0 1.0 2.5

velocity all create 1.0 12345 mom yes rot yes dist gaussian

fix 1 all nvt temp 0.7 0.7 1.0

dump 1 all custom 500 test.lammpstrj id type x y z vx vy vz
thermo 500

run 5000
```

密度0.5、同種原子はLJ、異種原子はWCAとして温度0.7に固定する。まずは短めに5000ステップだけにしておく。
後のために速度も出力しておく。

LAMMPSを実行する。

```sh
$ lmp_serial -i test.input
LAMMPS (20 Nov 2019)
Lattice spacing in x,y,z = 2 2 2
Created orthogonal box = (0 0 0) to (20 20 20)
  1 by 1 by 1 MPI processor grid
Created 4000 atoms
(snip)
Step Temp E_pair E_mol TotEng Press
       0            1    -1.505224            0 -0.005599034  -0.81748395
     500    1.0379285   -1.9071175            0    -0.350614   0.89774455
    1000    1.0320452   -1.9831115            0   -0.4354307   0.83759061
    1500    1.0048542   -2.0875114            0  -0.58060687   0.68268169
    2000   0.95389438   -2.1579864            0  -0.72750253    0.7033103
    2500   0.92615458   -2.2477533            0  -0.85886878   0.64168551
    3000   0.90328012   -2.3386703            0  -0.98408884   0.50502435
    3500   0.86221052   -2.4125228            0   -1.1195303   0.51427453
    4000   0.83401226    -2.485898            0   -1.2351923   0.41993354
    4500   0.82124657   -2.5744925            0   -1.3429306   0.37929561
    5000   0.80680117   -2.6549983            0   -1.4450991    0.3126729
(snip)
```

まずはこのサイズと原子数を取得する。`main.cpp`を以下のように書き換える。

```cpp
#include <cstdio>
#include <lammpstrj/lammpstrj.hpp>
#include <string>

int main() {
  const auto filename = "test.lammpstrj";
  auto si = lammpstrj::read_info(filename);
  printf("(LX, LY, LZ) = (%f, %f, %f)\n", si->LX, si->LY, si->LZ);
  printf("N = %d\n", si->atoms);
}
```

コンパイル、実行する。

```sh
$ make
$ ./lammpstrj-sample 
(LX, LY, LZ) = (20.000000, 20.000000, 20.000000)
N = 4000
```

情報が正しく取れている。

温度の取得。`main`関数の上に以下のような関数を作成。

```cpp
void calc_temperature(const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms) {
  static int frame_ = 0;
  double e = 0.0;
  for (auto &a : atoms) {
    e += a.vx * a.vx + a.vy * a.vy + a.vz * a.vz;
  }
  e /= static_cast<double>(si->atoms);
  e /= 3.0;
  printf("%d %f\n", frame_ * 500, e);
  frame_++;
}
```

`main`関数から`lammpstrj::for_each_fram`にファイル名と`calc_temperature`関数を渡して実行。

```cpp
int main() {
  const auto filename = "test.lammpstrj";
  auto si = lammpstrj::read_info(filename);
  printf("(LX, LY, LZ) = (%f, %f, %f)\n", si->LX, si->LY, si->LZ);
  printf("N = %d\n", si->atoms);
  lammpstrj::for_each_frame(filename, calc_temperature);
}
```

コンパイル、実行する。

```sh
$ make
$ ./lammpstrj-sample 
(LX, LY, LZ) = (20.000000, 20.000000, 20.000000)
N = 4000
0 0.999750
500 1.037669
1000 1.031787
1500 1.004603
2000 0.953656
2500 0.925923
3000 0.903054
3500 0.861995
4000 0.833804
4500 0.821041
5000 0.806599
```

先ほどのLAMMPSが出力した温度とほぼ同じ温度が出力されていることがわかる(1frameずれているのか、少しだけ値がずれる)。温度が取れている＝原子の情報を全て取得できているので、あとは好き勝手できる。

しかし、フレームがstatic変数になっているのがちょっと気持ち悪いのと、これからいろいろ情報が増えるので、クラスを作って、`calc_temperature`をメンバ関数とし、`frame_`や`filename_`をメンバ変数とする`LammpstrjAnalyzer`クラスを作る。

```cpp
class LammpstrjAnalyzer{
private:
  const std::string filename_;
  int frame_;

public:
  LammpstrjAnalyzer(const std::string filename): filename_(filename){
    frame_ = 0;
  }

  void calc_temperature(const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms) {
    double e = 0.0;
    for (auto &a : atoms) {
      e += a.vx * a.vx + a.vy * a.vy + a.vz * a.vz;
    }
    e /= static_cast<double>(si->atoms);
    e /= 3.0;
    printf("%d %f\n", frame_ * 500, e);
    frame_++;
  }

  void analyze(void){
    auto callback_function = [this](const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms){calc_temperature(si, atoms);};
    lammpstrj::for_each_frame(filename_, callback_function);
  }
};
```

ポイントは`analyze`関数。`lammpstrj::for_each_frame`にコールバック関数として`LammpstrjAnalyzer::calc_temperature`を渡したいが、直接は渡せない。そこで、一度ラムダ式でコールバック関数を作ってやり、その中でメンバ関数を呼ぶようにする。

```cpp
    auto callback_function = [this](const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms){calc_temperature(si, atoms);};
```

ここで作ったコールバック関数を`lammpstrj::for_each_frame`に渡せば良い。

```cpp
    lammpstrj::for_each_frame(filename_, callback_function);
```

一度`callback_function`という変数に受けなくても、いきなり

```cpp
lammpstrj::for_each_frame(filename_, [this](const std::unique_ptr<lammpstrj::SystemInfo> &si, const std::vector<lammpstrj::Atom> &atoms){calc_temperature(si, atoms);});
```

とできるが、可読性を考えると一度変数に受けた方が良い気がする。
