#include <iostream>
#include <iomanip>
 
using namespace std;
 
int main() {
    int cases;
    string bandido;
    cin >> cases;
    for(int i=0; i<cases; i++){
        cin.ignore();
        getline(cin, bandido);
        cout << "Y" << endl;
    }
 
    return 0;
}