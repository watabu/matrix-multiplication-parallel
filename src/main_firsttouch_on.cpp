#include "modules.hpp"

int num_threads;

double startTime, endTime;
double elapsedTime;

matrix multiply_matrix_firsttouch_on(matrix A, matrix B){
    int N,M,P;
    N = A.size();
    M = A[0].size();
    P = B[0].size();
    
    vector<vector<double>> C(N,vector<double>(P));

    // ファーストタッチ
    #pragma omp parallel for
        for(int i=0; i<N; i++) {
            for(int j=0; j<P; j++) {
                    C[i][j] = 0;
        }
    }

    startTime = omp_get_wtime();

    #pragma omp parallel for
    for(int i=0; i<N; i++) {
        for(int k=0; k<M; k++) {
            for(int j=0; j<P; j++) {
                C[i][j] = C[i][j] + A[i][k] *B[k][j];
            }
        }
    }
    endTime = omp_get_wtime();
    
    elapsedTime = endTime - startTime;
    printf("%.7f\n", elapsedTime);

    return C;
}

int main(){
    matrix A;
    matrix B;
    matrix C;

    cin >> num_threads;
    omp_set_num_threads(num_threads);
    
    A = input_matrix();
    B = input_matrix();

    // 行列のサイズが不正であれば中断
    if(can_multiply_matrix(A,B)==false){
        return -1;
    }

    C = multiply_matrix_firsttouch_on(A,B);

    cout << "C= \n";
    output_matrix(C);

    return 0;
}

