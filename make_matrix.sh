#!/bin/bash

# Usage: ./make_matrix.sh
# 各要素がランダムな行列と単位行列を作る

readonly EXE1=src/make_matrix_random.out
readonly EXE2=src/make_matrix_unit.out

readonly outputdir=input

# N M min_value max_value filename
readonly PARA_list1=(
    "3 3 -10 10 rand_3_3"
    "100 1 -100000 100000 rand_100_1"
    "100 10 -100000 100000 rand_100_10"
    "100 100 -100000 100000 rand_100_100"
    "100 1000 -100000 100000 rand_100_1000"
    "100 10000 -100000 100000 rand_100_10000"
    "1000 100 -100000 100000 rand_1000_100"
    "10000 100 -100000 100000 rand_10000_100"
    "200 100 -100000 100000 rand_200_100"
    "400 100 -100000 100000 rand_400_100"
    "800 100 -100000 100000 rand_800_100"
    "1600 100 -100000 100000 rand_1600_100"
    "4000 100 -100000 100000 rand_4000_100"
    "8000 100 -100000 100000 rand_8000_100"
)

# N M filename
readonly PARA_list2=(
    "3 3 unit_3"
    "100 100 unit_100"
)

# 行列をランダムに作る
for PARA in "${PARA_list1[@]}"
do
    echo $PARA
    NEWPARA=$(echo $PARA | awk '{print $1,$2,$3,$4}')
    N=$(echo $PARA | awk '{print $1}')
    M=$(echo $PARA | awk '{print $2}')
    filename=$(echo $PARA | awk '{print $5}')

    echo $N $M > $outputdir/$filename
    echo $NEWPARA | $EXE1 >> $outputdir/$filename
done

# 単位行列を作る
for PARA in "${PARA_list2[@]}"
do
    echo $PARA
    NEWPARA=$(echo $PARA | awk '{print $1,$2}')
    N=$(echo $PARA | awk '{print $1}')
    M=$(echo $PARA | awk '{print $2}')
    filename=$(echo $PARA | awk '{print $3}')

    echo $N $M > $outputdir/$filename
    echo $NEWPARA | $EXE2 >> $outputdir/$filename
done