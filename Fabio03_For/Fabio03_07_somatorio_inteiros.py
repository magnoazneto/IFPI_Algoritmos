from utilidades import get_inteiro
def main():
    limite = get_inteiro('Digite um número para o limite: ')
    contador = 1
    somatorio = 0
    while contador <= limite:
        somatorio += contador
        contador += 1
    print(f'Somatório: {somatorio}')


main()
