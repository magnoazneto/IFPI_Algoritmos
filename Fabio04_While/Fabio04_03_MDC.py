from utilidades import get_inteiro
def main():
    num1 = get_inteiro('Primeiro número: ')
    num2 = get_inteiro('Segundo número: ')
    print(f'MDC: {maximo_divisor_comum(num1, num2)}')


def maximo_divisor_comum(num1, num2):
    resto = num1 % num2
    while resto:
        num1 = num2
        num2 = resto
        resto = num1 % num2
    return num2 


main()
