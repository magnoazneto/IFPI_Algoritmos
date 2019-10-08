#include <iostream>
#include <math.h>

using namespace std;

int is_prime(int number){
    int i = 2;
    int divisores = 2;
    while (i <= (sqrt(number))){
        if (number % i == 0){
            divisores += 1;
        }
        if (divisores > 2){
            break;
        }
        i += 1;
    }
    if (divisores <= 2){
        return true;
    }
    else{
        return false;
    }
}


int main(){
    int testes, valor;
    cin >> testes;
    for (int i = 0; i < testes; i++){
        cin >> valor;
        if (is_prime(valor) == true){
            cout << "Prime" << endl;
        }
        else{
            cout << "Not Prime" << endl;
        }
    }
    return 0;
}