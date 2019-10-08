#include <iostream>

using namespace std;

int main(){
    int a, b;
    while (true){
        try{
            cin >> a >> b;
            //int resultado = a ^ b;
            if ((not(a)) || (not(b))){
                throw 1;
            }
            else{
                cout << (a ^ b) << endl;
            }
        }
        catch(int erro){
            if (erro == 1){
                break;
            }
        }
    }
    return 0;
}