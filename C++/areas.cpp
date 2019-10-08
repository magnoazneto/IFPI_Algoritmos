#include <iostream>
#include <iomanip>
//#include <math.h>

using namespace std;

int main(){
    int distancia;
    double combustivel;
    cin >> distancia >> combustivel;
    double consumo = distancia / combustivel;
    cout << fixed;
    cout << setprecision(3) << consumo << " km/l" << endl;
    return 0;
}


