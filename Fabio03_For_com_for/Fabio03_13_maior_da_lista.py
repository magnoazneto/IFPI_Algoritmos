from get_inputs import get_number, get_int_positivo
def main():
    tamanho = get_int_positivo('Tamanho da lista: ')
    maior = 0
    # while contador <= tamanho:
    for i in range(1, tamanho+1):
        valor_lido = get_number(f'{i}º valor: ')
        if valor_lido > maior:
            maior = valor_lido
    print(f'Maior número lido: {maior}')


main()