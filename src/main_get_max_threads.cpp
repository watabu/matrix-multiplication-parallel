#include <iostream>
#include <omp.h>
using namespace std;

int main(){    
    cout << omp_get_max_threads() << endl;
    
    return 0;
}

