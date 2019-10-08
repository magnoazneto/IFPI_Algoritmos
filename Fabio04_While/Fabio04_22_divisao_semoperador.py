from utilidades import get_inteiro
def main():
    num1 = get_inteiro('Digite o primeiro número: ')
    num2 = get_inteiro('Digite o segundo número: ')
    contador = 0
    while num1 >= num2:
        quociente = num1 - num2
        num1 = quociente
        contador += 1
    print(f'Quociente: {contador}')
    print(f'Resto: {quociente}')


main()
