#include <iostream>
#include <fstream>

using namespace std;

bool is_letter(char text){
    if ((int(text) >= 65) && (int(text) <= 90) || (int(text) >= 97) && (int(text) <= 122)){
        return true;
    }
    else {
        return false;
    }
}


void filter_string(string text){
    int i = 0;
    string new_str;
    bool error_one = false;
    while (i < text.length()){
        if ((text[i] == 'O') || (text[i] == 'o')){
            new_str += '0';
        }
        else if (text[i] == 'l'){
            new_str += '1';
        }
        else if (is_letter(text[i]) == true){
            cout << "error" << endl;
            error_one = true;
            break;
        }
        else if ((text[i]) == ',' || (text[i] == ' ')){
        }
        else{
            new_str += text[i];
        }
        i++;
    }
    //cout << text.length();
    if ((new_str.length() < 1) || (stol(new_str) > 2147483647)){
        if (not(error_one)){
            cout << "error" << endl;
        }
        //cout << "error" << endl;
    }
    else{
        cout << (stoi(new_str)) << endl;
    }
}


int main(){
    string number_text;
    while (true){
        if (getline(cin, number_text)){
            filter_string(number_text);
        }
        else if (cin.eof()){
            break;
        }
    }
    return 0;
}