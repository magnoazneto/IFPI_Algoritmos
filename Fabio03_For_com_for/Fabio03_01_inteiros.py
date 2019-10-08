from get_inputs import get_inteiro
def main():
    valor = get_inteiro('Por favor, digite um número inteiro: ')
    for i in range(1, valor+1):
        print(i, end = ' ')
    print()


main()