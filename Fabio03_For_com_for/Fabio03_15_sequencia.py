from get_inputs import get_int_positivo
def main():
    qtd = get_int_positivo('Digite a quantidade de termos: ')
    incremento = 2
    contador = numero = 1
    for i in range(1, qtd+1):
        print(numero, end = ' ')
        numero += incremento
        incremento += 1
    print()


main()
