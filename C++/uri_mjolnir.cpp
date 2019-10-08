#include <iostream>

using namespace std;

int main(){
    string name;
    int forca, cases;
    cin >> cases;
    for (int i=0; i < cases; i++){
        cin.ignore();
        getline(cin, name);
        cout << name << endl;
        if (name == "Thor"){
            cout << "Y" << endl;
        }
        else{
            cout << "N" << endl;
        }

    }

}