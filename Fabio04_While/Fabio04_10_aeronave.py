from utilidades import get_number, get_int_positivo, get_inteiro
def main():
    containers = get_int_positivo('Digite o número de containers: ')
    contador = 1
    peso_containers = passageiros = 0
    while contador <= containers:
        peso_containers += get_number(f'Peso do {contador} container: ')
        contador += 1
    contador = 1
    print('-----Dados dos passageiros-----')
    while True:
        bilhete = get_int_positivo('Bilhete:')
        if bilhete == 0: break
        passageiros += 1
        bagagens = get_inteiro('Quantidade de bagagens: ')
        bagagens *= 10 # consegue o peso em KG da bagagem
    passageiros_kg = passageiros * 70
    print('========= Relatório de voo =========')
    print(f'Quantidade de passageiros: {passageiros}')
    print(f'Volume de bagagens: {bagagens} KG')
    print(f'Peso dos passageiros: {passageiros_kg} KG')
    print(f'Peso da carga: {peso_containers}')
    total = bagagens + passageiros_kg + peso_containers
    print(f'Peso total: {total}')
    combustivel = 500000 - total
    combustivel = combustivel / 1.5
    print(f'É possível colocar {combustivel:.1f} L de combustível.')
    if combustivel >= 10000:
        print('É possível decolar!')
    else:
        print('Não é possível decolar.')
    

main()
