from utilidades import get_inteiro
def main():
    qtd = get_inteiro('Digite a quantidade de termos: ')
    incremento = 2
    contador = numero = 1
    while contador <= qtd:
        print(numero, end = ' ')
        numero += incremento
        incremento += 1
        contador += 1
    print()


main()
