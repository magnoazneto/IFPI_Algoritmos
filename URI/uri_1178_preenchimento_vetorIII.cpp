#include <iostream>
#include <iomanip>

using namespace std;

float porcentagem(float total, float qtd){
    return ((100.0*qtd) / total);
}

int main(){
    int total_saques = 0;
    int total_bloqueios = 0;
    int total_ataques = 0;
    int saques = 0;
    int bloqueios = 0;
    int ataques = 0;
    int cases;
    int tentativas[3];
    int resultados[3];
    cin >> cases;
    for (int i = 0; i < cases; i ++){
        string name;
        cin.ignore();
        getline(cin, name);
        cin >> tentativas[0] >> tentativas[1] >> tentativas[2];
        cin >> resultados[0] >> resultados[1] >> resultados[2];
        total_saques += tentativas[0];
        total_bloqueios += tentativas[1];
        total_ataques += tentativas[2];
        saques += resultados[0];
        bloqueios += resultados[1];
        ataques += resultados[2];
    }
    cout << fixed;
    cout << "Pontos de Saque: "<< setprecision(2) << (porcentagem(float(total_saques), float(saques))) << " %." << endl;
    cout << "Pontos de Bloqueio: " << setprecision(2) << (porcentagem(float(total_bloqueios), float(bloqueios))) << " %." << endl;
    cout << "Pontos de Ataque: " << setprecision(2) << (porcentagem(float(total_ataques), float(ataques))) << " %." << endl;
    return 0;

}
