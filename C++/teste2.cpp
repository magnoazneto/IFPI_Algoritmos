#include <iostream>
#include <iomanip>

using namespace std;

void print_cells(int money, int moedas){
    int notas_cem = money / 100;
    int notas_cinquenta = (money - notas_cem*100) / 50;
    int notas_vinte = (money - (notas_cem*100) - (notas_cinquenta*50)) / 20;
    int notas_dez = (money - (notas_cem*100) - (notas_cinquenta*50) - (notas_vinte*20)) / 10;
    int notas_cinco = (money - (notas_cem*100) - (notas_cinquenta*50) - (notas_vinte*20) - (notas_dez*10)) / 5;
    int notas_dois = (money - (notas_cem*100) - (notas_cinquenta*50) - (notas_vinte*20) - (notas_dez*10) - (notas_cinco*5)) / 2;
    int notas_um = (money - (notas_cem*100) - (notas_cinquenta*50) - (notas_vinte*20) - (notas_dez*10) - (notas_cinco*5) - (notas_dois*2));
    cout << "NOTAS:" << endl;
    cout << notas_cem << " nota(s) de R$ 100.00" << endl;
    cout << notas_cinquenta << " nota(s) de R$ 50.00" << endl;
    cout << notas_vinte << " nota(s) de R$ 20.00" << endl;
    cout << notas_dez << " nota(s) de R$ 10.00" << endl;
    cout << notas_cinco << " nota(s) de R$ 5.00" << endl;
    cout << notas_dois << " nota(s) de R$ 2.00" << endl;
    cout << "MOEDAS:" << endl;
    cout << notas_um << " moeda(s) de R$ 1.00" << endl;
    int moedas_cinquenta = moedas / 50;
    int moedas_vinte_cinto = (moedas - (moedas_cinquenta*50)) / 25;
    int moedas_dez = (moedas - (moedas_cinquenta*50) - (moedas_vinte_cinto*25)) / 10;
    int moedas_cinco = (moedas - (moedas_cinquenta*50) - (moedas_vinte_cinto*25) - (moedas_dez*10)) / 5;
    int moedas_um = (moedas - (moedas_cinquenta*50) - (moedas_vinte_cinto*25) - (moedas_dez*10) - (moedas_cinco*5));
    cout << moedas_cinquenta << " moeda(s) de R$ 0.50" << endl;
    cout << moedas_vinte_cinto << " moeda(s) de R$ 0.25" << endl;
    cout << moedas_dez << " moeda(s) de R$ 0.10" << endl;
    cout << moedas_cinco << " moeda(s) de R$ 0.05" << endl;
    cout << moedas_um << " moeda(s) de R$ 0.01" << endl;
}



int main(){
    double money;
    cin >> money;
    int moedas = int(money * 100) % 100;
    money = int(money);
    print_cells(money, moedas);
    return 0;
}
