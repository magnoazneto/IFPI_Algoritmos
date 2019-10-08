from get_inputs import get_number, get_int_positivo
def main():
    tamanho = get_int_positivo('Digite o tamanho da lista: ')
    somatorio = 0
    for i in range(1, tamanho+1):
        valor_lido = get_number(f'{i}º valor: ')
        somatorio += valor_lido
    print(f'Somatório: {somatorio}\nMédia: {somatorio/tamanho:.2f}')


main()