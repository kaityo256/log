---
title: "2025年7月28日"
date: 2025-07-28T00:00:00+09:00
lastmod: 2025-07-28T00:00:00+09:00
type: diary
source_month: "d202507.md"
generated: true
---

<!-- Generated from log/dYYYYMM.md. Do not edit directly. -->

物性研でのLAMMPSビルド。

```sh
git clone -b release --depth 1  https://github.com/lammps/lammps.git
cd lammps
cd src
module purge
module load aocc/4.0.0 openmpi/4.1.5-aocc-4.0
time make mpi CC=mpicxx LINK=mpicxx CCFLAGS="-g -O3 -std=c++11 -fopenmp" LINKFLAGS="-g -O3 -std=c++11 -fopenmp" -j 4
```

解析力学の問題ででた双子のパラドックスの解説がよくわからなかったので調べたが、やはり「折り返すあたりでおかしなことが起きる」という理解で正しいらしい。

```sh
$ module purge
$ module load aocc/4.0.0 openmpi/4.1.5-aocc-4.0
$ srun ~/usr/local/bin/lmp_mpi  < phase_separation.input 
LAMMPS (22 Jul 2025)
  using 1 OpenMP thread(s) per MPI task
Reading data file ...
  orthogonal box = (-40 -40 -40) to (40 40 40)
  4 by 4 by 8 MPI processor grid
  reading atoms ...
  256000 atoms
  reading velocities ...
  256000 velocities
  read_data CPU = 0.943 seconds
Generated 0 of 1 mixed pair_coeff terms from geometric mixing rule
Neighbor list info ...
  update: every = 1 steps, delay = 0 steps, check = yes
  max neighbors/atom: 2000, page size: 100000
  master list distance cutoff = 2.8
  ghost atom cutoff = 2.8
  binsize = 1.4, bins = 58 58 58
  1 neighbor lists, perpetual/occasional/extra = 1 0 0
  (1) pair lj/cut, perpetual
      attributes: half, newton on
      pair build: half/bin/atomonly/newton
      stencil: half/bin/3d
      bin: standard
Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 3.229 | 3.229 | 3.229 Mbytes
   Step          Temp          E_pair         E_mol          TotEng         Press     
         0   0.33307603    -1.516316       0             -1.0167039     -1.1601574    
      1000   0.87146409    -2.6897609      0             -1.3825698      0.38526114   
      2000   0.81123753    -3.1135239      0             -1.8966724      0.19467012   
      3000   0.7510551     -3.4628316      0             -2.3362533      0.080998673  
      4000   0.71569221    -3.7310777      0             -2.6575436      0.02935777   
      5000   0.70218845    -3.9131948      0             -2.8599162     -3.3590328e-05
      6000   0.69958594    -4.0285214      0             -2.9791466      0.0019604976 
      7000   0.69929718    -4.1104325      0             -3.0614908      0.00073366793
      8000   0.70048815    -4.1759958      0             -3.1252677     -0.014501419  
      9000   0.69942675    -4.2346808      0             -3.1855447     -0.012403831  
     10000   0.70026975    -4.2789932      0             -3.2285927     -0.013685938  
     11000   0.70028975    -4.3268318      0             -3.2764013     -0.010995688  
     12000   0.69958231    -4.3594105      0             -3.3100412     -0.0057749137 
     13000   0.69922989    -4.3923621      0             -3.3435214     -0.0058298883 
     14000   0.70132799    -4.4257153      0             -3.3737274     -0.0089451312 
     15000   0.69953001    -4.4560105      0             -3.4067196     -0.012706115  
     16000   0.69992825    -4.4876111      0             -3.4377228      0.0023749477 
     17000   0.70077277    -4.5137957      0             -3.4626407     -0.0052607339 
     18000   0.70010359    -4.5435306      0             -3.4933793     -0.017378879  
     19000   0.6986348     -4.5602393      0             -3.5122912      0.0031205848 
     20000   0.6997015     -4.5904728      0             -3.5409246     -0.012427492  
Loop time of 39.1545 on 128 procs for 20000 steps with 256000 atoms

Performance: 220664.164 tau/day, 510.797 timesteps/s, 130.764 Matom-step/s
99.5% CPU use with 128 MPI tasks x 1 OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 8.8906     | 14.499     | 17.607     |  43.1 | 37.03
Neigh   | 5.4021     | 8.2887     | 9.6775     |  27.5 | 21.17
Comm    | 6.6103     | 10.863     | 19.973     |  75.0 | 27.74
Output  | 0.47748    | 1.7681     | 3.0791     |  58.5 |  4.52
Modify  | 1.3164     | 2.0326     | 3.061      |  26.1 |  5.19
Other   |            | 1.704      |            |       |  4.35

Nlocal:           2000 ave        2618 max         710 min
Histogram: 1 3 2 8 13 15 18 26 22 20
Nghost:        3100.74 ave        3873 max        2046 min
Histogram: 2 3 6 16 18 22 23 17 12 9
Neighs:        57534.8 ave       81404 max       19211 min
Histogram: 3 2 5 14 10 22 19 28 12 13

Total # of neighbors = 7364453
Ave neighs/atom = 28.767395
Neighbor list builds = 2824
Dangerous builds = 0
Total wall time: 0:00:40
```

* 上記でビルドした奴
* 256000 atoms
* Total wall time: 0:00:40

```sh
$ source /home/issp/materiapps/intel/lammps/lammpsvars.sh
WARNING: Preinstalled software under /home/issp/materiapps/intel may not work well
         because the old Intel compiler and environment are no longer available
         due to the vulenerability from April 2023.
         Insteadly, please use software under
         /home/issp/materiapps/oneapi_compiler_classic-2023.0.0--openmpi-4.1.5
$ srun lammps < phase_separation.input 
LAMMPS (23 Jun 2022 - Update 1)
  using 1 OpenMP thread(s) per MPI task
Reading data file ...
  orthogonal box = (-40 -40 -40) to (40 40 40)
  4 by 4 by 8 MPI processor grid
  reading atoms ...
  256000 atoms
  reading velocities ...
  256000 velocities
  read_data CPU = 2.224 seconds
Generated 0 of 1 mixed pair_coeff terms from geometric mixing rule
Neighbor list info ...
  update every 1 steps, delay 10 steps, check yes
  max neighbors/atom: 2000, page size: 100000
  master list distance cutoff = 2.8
  ghost atom cutoff = 2.8
  binsize = 1.4, bins = 58 58 58
  1 neighbor lists, perpetual/occasional/extra = 1 0 0
  (1) pair lj/cut, perpetual
      attributes: half, newton on
      pair build: half/bin/atomonly/newton
      stencil: half/bin/3d
      bin: standard
Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 4.306 | 4.306 | 4.306 Mbytes
   Step          Temp          E_pair         E_mol          TotEng         Press     
         0   0.33307603    -1.516316       0             -1.0167039     -1.1601574    
      1000   0.87146409    -2.6897609      0             -1.3825698      0.38526114   
      2000   0.80962765    -3.1111547      0             -1.8967179      0.19000521   
      3000   0.75045823    -3.4638154      0             -2.3381324      0.070515194  
      4000   0.71566284    -3.7342073      0             -2.6607173      0.029782565  
      5000   0.70476387    -3.9191839      0             -2.8620423      0.010235361  
      6000   0.70002178    -4.0315351      0             -2.9815066     -0.0023020533 
      7000   0.69981926    -4.1168468      0             -3.067122       0.0050582736 
      8000   0.69854175    -4.1865747      0             -3.1387661     -0.0058356486 
      9000   0.69866897    -4.2469661      0             -3.1989668     -0.0064063014 
     10000   0.70036779    -4.2888114      0             -3.2382638     -0.0063266451 
     11000   0.69836934    -4.3444797      0             -3.2969298     -0.0080423013 
     12000   0.70151992    -4.3749402      0             -3.3226644     -0.011008209  
     13000   0.69913454    -4.411778       0             -3.3630803     -0.0098862328 
     14000   0.69903093    -4.4429242      0             -3.3943819     -0.010131298  
     15000   0.70053583    -4.4741996      0             -3.4233999     -0.012884346  
     16000   0.69868448    -4.5000671      0             -3.4520444     -0.014619224  
     17000   0.7005849     -4.5230098      0             -3.4721366     -0.011477545  
     18000   0.69949419    -4.540732       0             -3.4914948     -0.0068405286 
     19000   0.70035761    -4.5630048      0             -3.5124725     -0.0082542691 
     20000   0.69967689    -4.5866956      0             -3.5371843     -0.0059617226 
Loop time of 182.152 on 128 procs for 20000 steps with 256000 atoms

Performance: 47432.855 tau/day, 109.798 timesteps/s
96.3% CPU use with 128 MPI tasks x 1 OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 15.524     | 24.057     | 28.719     |  55.4 | 13.21
Neigh   | 3.9487     | 5.7312     | 6.8138     |  24.5 |  3.15
Comm    | 57.198     | 88.669     | 123.09     | 168.2 | 48.68
Output  | 6.2454     | 32.804     | 59.523     | 275.8 | 18.01
Modify  | 25.603     | 29.808     | 35.164     |  36.0 | 16.36
Other   |            | 1.083      |            |       |  0.59

Nlocal:           2000 ave        2697 max         731 min
Histogram: 2 0 9 7 11 18 19 28 29 5
Nghost:         3165.7 ave        3959 max        2059 min
Histogram: 2 3 8 8 22 25 19 23 14 4
Neighs:        57489.3 ave       84939 max       15694 min
Histogram: 1 1 11 6 16 19 29 25 16 4

Total # of neighbors = 7358635
Ave neighs/atom = 28.744668
Neighbor list builds = 1998
Dangerous builds = 1994
Total wall time: 0:03:06
```

なんでこんなに遅いんだ？

温度制御なし、ダンプなしでやってみる。

```sh
$ srun lammps < phase_separation.input 
LAMMPS (23 Jun 2022 - Update 1)
  using 1 OpenMP thread(s) per MPI task
Reading data file ...
  orthogonal box = (-40 -40 -40) to (40 40 40)
  4 by 4 by 8 MPI processor grid
  reading atoms ...
  256000 atoms
  reading velocities ...
  256000 velocities
  read_data CPU = 0.717 seconds
Generated 0 of 1 mixed pair_coeff terms from geometric mixing rule
Neighbor list info ...
  update every 1 steps, delay 10 steps, check yes
  max neighbors/atom: 2000, page size: 100000
  master list distance cutoff = 2.8
  ghost atom cutoff = 2.8
  binsize = 1.4, bins = 58 58 58
  1 neighbor lists, perpetual/occasional/extra = 1 0 0
  (1) pair lj/cut, perpetual
      attributes: half, newton on
      pair build: half/bin/atomonly/newton
      stencil: half/bin/3d
      bin: standard
Setting up Verlet run ...
  Unit style    : lj
  Current step  : 0
  Time step     : 0.005
Per MPI rank memory allocation (min/avg/max) = 3.229 | 3.229 | 3.229 Mbytes
   Step          Temp          E_pair         E_mol          TotEng         Press     
         0   0.33307603    -1.516316       0             -1.0167039     -1.1601574    
      1000   0.97815002    -2.6011809      0             -1.1339616      0.52297807   
      2000   1.0779394     -2.7468018      0             -1.1298991      0.5633349    
      3000   1.1282011     -2.8204732      0             -1.1281782      0.56862548   
      4000   1.156782      -2.8627757      0             -1.1276094      0.57878785   
      5000   1.1758223     -2.8912819      0             -1.1275553      0.57678955   
      6000   1.1910381     -2.9150934      0             -1.1285432      0.56857324   
      7000   1.2023978     -2.9315842      0             -1.1279945      0.5805573    
      8000   1.207307      -2.9386324      0             -1.127679       0.57309582   
      9000   1.2193711     -2.9575387      0             -1.1284892      0.57309902   
     10000   1.2241679     -2.9644462      0             -1.1282014      0.57488072   
     11000   1.2305362     -2.9734281      0             -1.127631       0.56729845   
     12000   1.2371822     -2.9826972      0             -1.1269312      0.56772114   
     13000   1.2407996     -2.9885648      0             -1.1273726      0.57271685   
     14000   1.2459587     -2.9959874      0             -1.1270567      0.55516076   
     15000   1.2478928     -2.9990612      0             -1.1272293      0.56499782   
     16000   1.2498853     -3.0025854      0             -1.1277648      0.5536481    
     17000   1.2540465     -3.0078717      0             -1.1268094      0.56287692   
     18000   1.2549821     -3.009273       0             -1.1268071      0.55989435   
     19000   1.2571933     -3.0127934      0             -1.1270108      0.55622421   
     20000   1.2611402     -3.0186255      0             -1.1269226      0.55445958   
Loop time of 77.7506 on 128 procs for 20000 steps with 256000 atoms

Performance: 111124.505 tau/day, 257.233 timesteps/s
95.0% CPU use with 128 MPI tasks x 1 OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 17.788     | 19.366     | 20.743     |  14.1 | 24.91
Neigh   | 5.1141     | 5.4157     | 5.8469     |   6.9 |  6.97
Comm    | 49.704     | 51.449     | 53.18      |  10.4 | 66.17
Output  | 0.0035131  | 0.0037755  | 0.004142   |   0.3 |  0.00
Modify  | 0.42471    | 0.4391     | 0.45213    |   0.9 |  0.56
Other   |            | 1.077      |            |       |  1.39

Nlocal:           2000 ave        2132 max        1894 min
Histogram: 6 11 19 22 18 23 12 8 7 2
Nghost:        3117.23 ave        3246 max        2993 min
Histogram: 3 10 13 14 23 24 20 15 4 2
Neighs:        41621.2 ave       47436 max       36409 min
Histogram: 5 12 11 24 18 22 17 7 3 9

Total # of neighbors = 5327513
Ave neighs/atom = 20.810598
Neighbor list builds = 1998
Dangerous builds = 1994
Total wall time: 0:01:18
```

二回目。

```sh
Total wall time: 0:01:19
```

```sh
$ module purge
$ module load aocc/4.0.0 openmpi/4.1.5-aocc-4.0
$ srun ~/usr/local/bin/lmp_mpi  < phase_separation.input 
Total wall time: 0:00:32
```

二回目。

```sh
Total wall time: 0:00:31
```

うお、三倍くらい早い。

2ノード。

```sh
$ salloc -N 2 -n 256 -p i8cpu
Total wall time: 0:00:21
```

2度目。

```sh
Total wall time: 0:00:19
```

1ノード128プロセスから2ノード256プロセスで1.5倍。まぁそんなものだろう。

```sh
$ module list
Currently Loaded Modulefiles:
 1) oneapi_compiler/2023.0.0   2) oneapi_mpi/2023.0.0  
Total wall time: 0:01:40
```

まとめると、

* ビルドしたLAMMPS (LAMMPS (22 Jul 2025)
    * 1ノード128プロセス：32秒
    * 2ノード256プロセス：20秒
* デフォルトのLAMMPS (LAMMPS (23 Jun 2022 - Update 1))
    * 1ノード128プロセス：78秒
    * 2ノード256プロセス：96秒

ビルドした奴の方が数倍早いな。

数理物理期末テスト。半分くらい採点したが、かなりよくできている。難易度は例年並みだと思うのだが。
