#include <iostream>
#include <iomanip>

using namespace std;

int remove_diamantes(string mina){
    int esquerda = 0, diamantes = 0;
    for (int i = 0; i < mina.length(); i++){
        if (mina[i] == '<'){
            esquerda = true;
        }
        else{
            esquerda = false;
        }
        if (esquerda == true){
            for (int d = i; d < mina.length(); d++){
                if (mina[d] == '>'){
                    mina[i] = 'w';
                    mina[d] = mina[i];
                    diamantes += 1;
                    esquerda = false;
                    break;
                }
            }
        }
    }
    return diamantes;
}


int main(){
    int cases;
    char mina[1000];
    cin >> cases;
    for (int i=0; i<cases; i++){
        cin >> mina;
        cout << remove_diamantes(mina) << endl;
    }

    return 0;
}