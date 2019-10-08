from utilidades import get_inteiro
def main():
    limite_sup = get_inteiro('Digite o limite superior: ')
    limite_inf = get_inteiro('Digite o limite inferior: ')
    while limite_inf <= limite_sup:
        if limite_inf % 2 != 0: print(limite_inf, end = ' ')
        limite_inf += 1
    print()


main()