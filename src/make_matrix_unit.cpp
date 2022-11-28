#include "modules.hpp"
#include <random>
using namespace std;

// 単位行列を作る
matrix generate_matrix_unit(int N,int M){
    vector<vector<double>> A(N,vector<double>(M));

    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            A[i][j] = (i == j) ? 1 : 0;
        }
    }    
    return A;
}

int main(){
    int N, M;
    double min_value, max_value;
    //int min_value, max_value;

    cin >> N >> M;

    matrix A = generate_matrix_unit(N,M);

    output_matrix(A);
    
    return 0;
}

