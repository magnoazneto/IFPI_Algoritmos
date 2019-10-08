#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

int main(){
    double pi = 3.14159;
    double raio, area;
    cin >> raio;
    area = pi * pow(raio, 2);
    cout << fixed;
    cout << "A=" << setprecision(4) << area << endl;
    return 0;
}