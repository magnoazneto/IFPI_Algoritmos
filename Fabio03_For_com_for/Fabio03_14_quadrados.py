from get_inputs import get_inteiro
from math import sqrt
def main():
    numero = get_inteiro('Digite um número para análise: ')
    maior = 1
    for i in range(numero, 1, -1):
        if (sqrt(i) % 1 == 0):
            maior = i
            break
    print(f'Maior quadrado: {maior}')
    print(f'{int(sqrt(maior))}**2 = {maior}')


main()