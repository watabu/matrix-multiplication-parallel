#!/bin/bash

# Usage: ./run_test_strong_scaling.sh
# 行列積プログラムのストロングスケーリングを求める
# ストロングスケーリング：同じ問題サイズについて並列度を変えていき，実行時間の短縮度合いを見る

readonly EXE=src/main_firsttouch_off.out
#readonly EXE=src/main_firsttouch_on.out

readonly matrixA=input/rand_1000_100
readonly matrixB_list="
    input/rand_100_1
    input/rand_100_10
    input/rand_100_100"
    
readonly num_threads_list="1 2 4 8 16 40 80"

readonly outfile=output/scaling_strong.csv

# 列名
echo "matrixA matrixB" $num_threads_list > $outfile

#　行列積
# space-separatedのcsvになるように整形してファイルに出力
for matrixB in $matrixB_list
do
    echo -n $matrixA $matrixB " "
    for num_threads in $num_threads_list
    do    
        $EXE <<< $(echo $num_threads $(cat $matrixA $matrixB)) | head -n 1
        echo -n " "
    done | tr -d '\n'
    echo ""
done | sed -e "s/ \+/ /g" | sed -e "s/ $//g" >> $outfile

