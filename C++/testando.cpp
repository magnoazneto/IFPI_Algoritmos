#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;


string fill_with(string text, char filler, int tam){
    string result;
    for (int i=0; i<(tam-(text.length())); i++){
        result += filler;
    }
    result = result + text;
    return result;    
}

int main(){
    vector <string> names;
    string nameInput;
    int cases, bigger;
    cin >> cases;
    while (cases != 0){
        names = {};
        bigger = 0;
        cin.ignore();
        for (int i=0; i < cases; i++){
            getline(cin, nameInput);
            names.push_back(nameInput);
            if ((nameInput.length()) > bigger){
                bigger = nameInput.length();
            }
        }

        for (int i=0; i < cases; i++){
            cout << fill_with(names[i], ' ', bigger) << endl;
        }

        cin >> cases;
        if (cases == 0){
            break;
        }
        cout << endl;

    }

    return 0;
}