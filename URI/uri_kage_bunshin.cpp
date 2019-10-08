#include <iostream>
#include <math.h>

using namespace std;

bool eh_retangulo(float a, float b, float c){
    if ((pow(a,2) == pow(b,2) + pow(c, 2)) || (pow(b,2) == pow(a,2) + pow(c, 2)) || (pow(c,2) == pow(b,2) + pow(a, 2))){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    if (( a + b > c) || ( b + c > a) || ( a + c > b)){
        cout << "Invalido" << endl;
    }
    else if (a == b == c){
        cout << "Valido-Equilatero" << endl;
        if (eh_retangulo(a,b,c)){
            cout << "Retangulo: S" << endl;
        }
        else{
            cout << "Retangulo: N" << endl;
        }
    }
    else if ((a == b) || (a == c) || (b == c)){
        cout << "Valido-Isoceles" << endl;
        if (eh_retangulo(a,b,c)){
            cout << "Retangulo: S" << endl;
        }
        else{
            cout << "Retangulo: N" << endl;
        }
    }
    else{
        cout << "Valido-Escaleno" << endl;
        if (eh_retangulo(a,b,c)){
            cout << "Retangulo: S" << endl;
        }
        else{
            cout << "Retangulo: N" << endl;
        }
    }

    return 0;
}