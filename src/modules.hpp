#ifndef _H_MODULES_
#define _H_MODULES_

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iostream>
#include <vector>
#include <omp.h>
using namespace std;

typedef vector<vector<double>> matrix;

matrix input_matrix();
void output_matrix(matrix A);

// 行列積が可能か確認
bool can_multiply_matrix(matrix A, matrix B);

matrix multiply_matrix(matrix A, matrix B);


#endif