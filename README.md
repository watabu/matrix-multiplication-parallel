# matrix-multiplication-parallel
行列積プログラムをOpenMPを用いて並列実行し．並列数ごとの性能を実行時間，速度向上率，並列化効率で評価します．

## Usage

まずはじめに src 内で make します．
```
cd src
make
cd -
```

現在の実行環境の最大スレッド数を確認します．
```
./check_max_num_threads.sh
```
以降，最大並列数に応じてシェルスクリプトの`readonly num_threads_list="1 2 4 8 16 40 80"`を書き換えてください．  
例えば最大並列数が16の場合は`readonly num_threads_list="1 2 4 8 16"`などに書き換えてください．



行列積プログラムの簡易実行をします．
run_sample3.shはnum_threads_listを適宜書き換えてください．
```
./run_sample1.sh
./run_sample2.sh
./run_sample3.sh
```
並列数と行列積の処理にかかった時間や行列積の結果が出力されます．

並列数によるスケーリング効果をストロングスケーリング，ウィークスケーリングで評価します．
num_threads_listは適宜書き換えてください．
```
./run_test_scaling_strong.sh
./run_test_scaling_weak.sh
```
結果がoutput/scaling_strong.csv,output/scaling_weak.csvに出力されているはずです．

ストロングスケーリングとウィークスケーリングをグラフで可視化します．
```
./make_graph.sh
```

