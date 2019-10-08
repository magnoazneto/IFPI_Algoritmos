from get_inputs import get_inteiro
def main():
    valor = get_inteiro('Por favor, digite um número inteiro: ')
    for contador in range(1, valor+1):
        if contador % 2 == 0: print(contador, end = ' ')
    print()


main()