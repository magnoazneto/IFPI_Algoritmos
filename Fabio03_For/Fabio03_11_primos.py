from utilidades import get_inteiro
def main():
    limite_sup = get_inteiro('Digite o limite superior: ')
    limite_inf = get_inteiro('Digite o limite inferior: ')
    while limite_inf <= limite_sup:
        if primo(limite_inf): print(limite_inf, end = ' ')
        limite_inf += 1
    print()


def primo(valor):  # checa se um valor é primo ou não
    total = 0
    contador = 1
    while contador <= valor:
        if valor % contador == 0: total += 1
        contador += 1
    return True if total == 2 else False


main()