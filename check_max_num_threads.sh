#!/bin/bash

# Usage: ./check_max_num_threads.sh
# 現在の環境で使える最大並列スレッド数を出力する

readonly EXE=src/main_get_max_threads.out

$EXE
