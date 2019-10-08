from utilidades import get_number, get_int_positivo
def main():
    tamanho = get_int_positivo('Tamanho da lista: ')
    contador = 1
    maior = 0
    while contador <= tamanho:
        valor_lido = get_number(f'{contador}º valor: ')
        if valor_lido > maior:
            maior = valor_lido
        contador += 1
    print(f'Maior número lido: {maior}')


main()