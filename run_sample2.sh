#!/bin/bash

# Usage: ./run_sample2.sh
# 行列ファイルA，Bの積を実行し，実行時間と積の結果を出力する

readonly EXE=src/main_firsttouch_off.out
#readonly EXE=src/main_firsttouch_on.out

#readonly matrixA=input/unit_3
#readonly matrixB=input/unit_3
readonly matrixA=input/rand_3_3
readonly matrixB=input/unit_3

# 並列度
readonly num_threads=4

echo -n $num_threads " "
echo $num_threads $(cat $matrixA $matrixB) | $EXE | head -n 1
