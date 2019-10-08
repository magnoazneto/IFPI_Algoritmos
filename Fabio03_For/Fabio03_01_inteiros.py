from utilidades import get_inteiro
def main():
    contador = 1
    valor = get_inteiro('Por favor, digite um número inteiro: ')
    while contador <= valor:
        print(contador, end = ' ')
        contador += 1
    print()


main()