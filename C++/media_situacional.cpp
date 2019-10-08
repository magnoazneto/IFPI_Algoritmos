#include <iostream>
#include <math.h>
#include <iomanip>

using namespace std;

float calcula_media(float n1, float n2, float n3, float n4){
    return ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10;
}


int main(){
    float n1, n2, n3, n4;
    float exame;
    cin >> n1 >> n2 >> n3 >> n4;
    float media = calcula_media(n1, n2, n3, n4);
    cout << fixed;
    cout << "Media: " << setprecision(1) << media << endl;
    if (media >= 7){
        cout << "Aluno aprovado." << endl;
    }
    else if (media >= 5){
        cout << "Aluno em exame." << endl;
        cin >> exame;
        cout << fixed;
        cout << "Nota do exame: " << setprecision(1) << exame << endl;
        media = (media + exame) / 2;
        if (media >= 5){
            cout << "Aluno aprovado." << endl;
        }
        else{
            cout << "Aluno reprovado." << endl;;
        }
        cout << fixed;
        cout << "Media final: " << setprecision(1) << media << endl;
    }
    else{
        cout << "Aluno reprovado." << endl;
    }

    return 0;
}