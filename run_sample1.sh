#!/bin/bash

# Usage: ./run_sample2.sh
# 行列の積を実行し，実行時間と積の結果を出力する

readonly EXE=src/main_firsttouch_off.out
#readonly EXE=src/main_firsttouch_on.out

# 並列度
readonly num_threads=3

# １つ目の行列
readonly matrixA="
    3 3
    1 2 3
    4 5 6
    7 8 9"
# ２つ目の行列
readonly matrixB="
    3 3
    0 1 0
    1 0 0
    0 0 1"

echo -n $num_threads " "
echo $num_threads $matrixA $matrixB | $EXE
