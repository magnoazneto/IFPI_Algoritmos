from utilidades import get_int_positivo
def main():
    den_atual = get_int_positivo('Digite o primeiro denominador: ')
    numerador = 1
    somatorio = 0
    while den_atual >= 1:
        somatorio += (numerador/den_atual)
        den_atual -= numerador
        numerador += 1
    print(f'Somatório: {somatorio:.2f}')
    

main()
