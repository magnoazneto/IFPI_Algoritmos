from utilidades import get_inteiro
from math import sqrt
def main():
    numero = get_inteiro('Digite um número para análise: ')
    maior = 1
    while numero >= 1:
        if (sqrt(numero)*10) % 10 == 0:
            maior = numero
            break
        numero -= 1
    print(f'Maior quadrado: {maior}')
    print(f'{int(sqrt(maior))}**2 = {maior}')


main()