#include "modules.hpp"
#include <random>
using namespace std;

matrix generate_matrix_random_int(int N,int M, int min_value, int max_value){
    vector<vector<double>> A(N,vector<double>(M));
    
    std::random_device rnd;
    std::mt19937 mt(rnd());
    std::uniform_int_distribution<> rand_range(min_value, max_value);

    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            A[i][j] = rand_range(mt);
        }
    }
    
    return A;
}

// N×Mの行列を作る　値の範囲を指定
matrix generate_matrix_random_double(int N,int M, double min_value, double max_value){
    vector<vector<double>> A(N,vector<double>(M));
    
    std::random_device rnd;
    std::mt19937 mt(rnd());
    std::uniform_real_distribution<> rand_range(min_value, max_value); 

    for(int i=0;i<N;++i){
        for(int j=0;j<M;++j){
            A[i][j] = rand_range(mt);
        }
    }
    
    return A;
}

int main(){
    int N, M;
    double min_value, max_value;
    //int min_value, max_value;

    cin >> N >> M;
    cin >> min_value >> max_value;

    matrix A = generate_matrix_random_double(N,M,min_value,max_value);

    output_matrix(A);
    
    return 0;
}

