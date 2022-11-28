#include "modules.hpp"

matrix input_matrix(){
    int N,M;
    cin >> N >> M;

    vector<vector<double>> A(N,vector<double>(M));
    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            cin >> A[i][j];
        }
    }

    return A;
}

void output_matrix(matrix A){
    int N,M;
    N = A.size();
    M = A[0].size();

    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}

// 行列積が可能か確認
bool can_multiply_matrix(matrix A, matrix B){
    //int N_a = A.size();
    int M_a = A[0].size();
    int M_b = B.size();
    //int P_b = B[0].size();

    if(M_a != M_b){
        cout << "Error: matrix shape is not match\n";
        return false;
    }
    return true;
}

// 何の工夫もない単純な行列積
matrix multiply_matrix(matrix A, matrix B){
    int N,M,P;
    N = A.size();
    M = A[0].size();
    P = B[0].size();
    
    vector<vector<double>> C(N,vector<double>(P));

    for(int i=0; i<N; i++) {
        for(int j=0; j<P; j++) {
            for(int k=0; k<M; k++) {
                C[i][j] = C[i][j] + A[i][k] *B[k][j];
            }
        }
    }
    return C;
}


