from utilidades import get_inteiro
def main():
    num = get_inteiro('Digite um número: ')
    if num < 0: num *= -1
    digitos = 1
    while num // 10 > 0:
        num = num // 10
        digitos += 1
    print(f'Número de dígitos: {digitos}')


main()
