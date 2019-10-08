from utilidades import get_number, get_inteiro
def main():
    fichas = get_inteiro('Quantas fichas irá avaliar? ')
    magro, id_magro, gordo, id_gordo = filtro_bois(fichas)
    print(f'Boi mais magro: {id_magro}, com {magro} KG')
    print(f'Boi mais gordo: {id_gordo}, com {gordo} KG')


def filtro_bois(fichas):
    contador = 1
    peso = 0.0
    nome = ' '
    ident = gordo = id_magro = id_gordo = 0
    magro = 200000

    while contador <= fichas:
        ident = get_inteiro(f'ID do {contador}º boi: ')
        nome = input(f'Nome do {contador}º boi: ')
        peso = get_number(f'Peso em KG do {contador}º boi: ')
        if peso > gordo:
            gordo = peso
            id_gordo = ident
        if peso < magro:
            magro = peso
            id_magro = ident
        contador += 1
    return magro, id_magro, gordo, id_gordo


main()
