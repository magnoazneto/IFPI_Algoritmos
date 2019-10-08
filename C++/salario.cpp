#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main(){
    double raio, pi = 3.14159;
    cin >> raio;
    double volume = (4.0/3) * pi * pow(raio, 3);
    cout << fixed;
    cout << "VOLUME = " << setprecision(3) << volume << endl;
    return 0;
}