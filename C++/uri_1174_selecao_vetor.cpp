#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float numbers[100];
    for (int i=0; i<100; i++){
        cin >> numbers[i];
    }
    for (int i=0; i<100; i++){
        if (numbers[i] <= 10){
            printf("A[%i] = %.1f\n", i, numbers[i]);
        }
    }

    return 0;
}