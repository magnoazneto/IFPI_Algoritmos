from get_inputs import get_inteiro
def main():
    limite_sup = get_inteiro('Digite o limite superior: ')
    limite_inf = get_inteiro('Digite o limite inferior: ')
    for i in range(limite_inf, limite_sup+1):
        if i % 2 == 0: print(i, end = ' ')
    print()


main()