from utilidades import get_int_positivo
def main():
    den_final = get_int_positivo('Digite o ultimo denominador: ')
    den_atual = 1
    somatorio = 0
    while den_atual <= den_final:
        somatorio += (1/den_atual)
        den_atual += 1
    print(f'Somatório: {somatorio:.2f}')
    

main()
