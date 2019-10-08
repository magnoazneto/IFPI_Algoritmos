from get_inputs import get_inteiro
def main():
    numero = get_inteiro('Digite um número N: ')
    limite_inferior = get_inteiro('Digite o limite inferior: ')
    limite_superior = get_inteiro('Digite o limite superior: ')
    indice = 1
    for i in range(limite_inferior, limite_superior+1):
        if i % numero == 0:
            print(f'{indice}º múltiplo: {i}')
            indice += 1  


main()
