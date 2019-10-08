from utilidades import get_number
def main():
    x = get_number('Digite o valor de X: ')
    n = get_number('Digite o valor de N: ')
    resultado = 0
    while n > 2:
        resultado = x / n
        print(f'{resultado:.4f}')
        x = resultado
        n -= 1


main()
