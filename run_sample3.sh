#!/bin/bash

# Usage: ./run_sample3.sh
# 行列ファイルA，Bの積を各並列度について実行し，実行時間を出力する

readonly EXE=src/main_firsttouch_off.out
#readonly EXE=src/main_firsttouch_on.out

#readonly matrixA=input/unit_3
#readonly matrixB=input/unit_3
readonly matrixA=input/rand_400_100
readonly matrixB=input/rand_100_1000

readonly num_threads_list="1 2 4 8 16 40 80"

for num_threads in $num_threads_list
do    
    echo -n $num_threads " "
    echo $num_threads $(cat $matrixA $matrixB) | $EXE | head -n 1
done

