from utilidades import get_float_positivo
def main():
    num = get_float_positivo('Digite um número maior ou igual a 1: ')
    while num >= 1:
        num /= 2
    print(f'Resultado final: {num:.2f}')    


main()
