#!/bin/bash

# Usage: ./make_graph.sh
# run_test_scaling_strong.sh,run_test_scaling_weak.shの出力ファイルからグラフを作る

readonly csvfile_strong=output/scaling_strong.csv
readonly csvfile_weak=output/scaling_weak.csv

python postprocess/make_graph_scaling_strong.py $csvfile_strong
python postprocess/make_graph_scaling_weak.py $csvfile_weak


