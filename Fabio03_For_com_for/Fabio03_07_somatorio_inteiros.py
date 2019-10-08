from get_inputs import get_int_positivo
def main():
    limite = get_int_positivo('Digite um número para o limite: ')
    somatorio = 0
    for contador in range(1, limite+1):
        somatorio += contador
    print(f'Somatório: {somatorio}')


main()
