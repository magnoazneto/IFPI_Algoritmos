from utilidades import get_number
def main():
    tamanho = get_number('Digite o tamanho da lista: ')
    contador = 1
    somatorio = 0
    while contador <= tamanho:
        valor_lido = get_number(f'{contador}º valor: ')
        somatorio += valor_lido
        contador += 1
    print(f'Somatório: {somatorio}\nMédia: {somatorio/tamanho:.2f}')


main()