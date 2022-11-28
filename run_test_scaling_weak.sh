#!/bin/bash

# Usage: ./run_test_strong_scaling.sh
# 行列積プログラムのウィークスケーリングを求める
# ウィークスケーリング：各プロセッサの問題サイズが等しくなるように合計問題サイズと並列数を変えていき，実行時間の増え具合を見る

readonly EXE=src/main_firsttouch_off.out
#readonly EXE=src/main_firsttouch_on.out

readonly matrixA_head="input/rand_"
readonly matrixA_tail="_100"
    
readonly matrixB_list="
    input/rand_100_1
    input/rand_100_10
    input/rand_100_100
    input/rand_100_1000"

readonly num_threads_list="1 2 4 8 16 40 80"

readonly outfile=output/scaling_weak.csv

# 列名
echo "matrixB" $num_threads_list > $outfile

#　行列積
# space-separatedのcsvになるように整形してファイルに出力
for matrixB in $matrixB_list
do
    echo -n $matrixB " "
    for num_threads in $num_threads_list
    do
        # 並列度にあわせたファイルを選択
        matrixA="${matrixA_head}${num_threads}00${matrixA_tail}"

        echo $num_threads $(cat $matrixA $matrixB) | $EXE | head -n 1
        echo -n " "
    done | tr -d '\n'
    echo ""
done | sed -e "s/ \+/ /g" | sed -e "s/ $//g" >> $outfile



