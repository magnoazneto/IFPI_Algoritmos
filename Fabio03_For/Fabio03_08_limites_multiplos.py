from utilidades import get_inteiro
def main():
    numero = get_inteiro('Digite um número N: ')
    limite_superior = get_inteiro('Digite o limite superior: ')
    limite_inferior = get_inteiro('Digite o limite inferior: ')
    indice = 1
    while limite_inferior <= limite_superior:
        if limite_inferior % numero == 0:
            print(f'{indice}º múltiplo: {limite_inferior}')
            indice += 1
        limite_inferior +=1    


main()
