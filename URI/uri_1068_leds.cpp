#include <iostream>

using namespace std;

int filtro(char numero){
    if (numero == 1){
        return 2;
    }
    else if ((numero == 2) || (numero == 3) || (numero == 5)){
        return 5;
    }
    else if (numero == 4){
        return 4;
    }
    else if ((numero == 6) || (numero == 9) || (numero == 0)){
        return 6;
    }
    else if (numero == 7){
        return 3;
    }
    else if (numero == 8){
        return 7;
    }
}

int main(){
    int cases, somatorio;
    char numero[101];
    cin >> cases;
    for (int i=0; i<cases; i++){
        cin >> numero;
        cout << (int)strlen(numero) << end;
        for (int c=0; c < strlen(numero); c++){
            somatorio += filtro(numero[c]);
        }
        cout << somatorio << " leds" << endl;
        somatorio = 0;
    }

    return 0;
}