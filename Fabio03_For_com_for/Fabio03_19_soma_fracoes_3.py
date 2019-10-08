from get_inputs import get_int_positivo
def main():
    num_final = get_int_positivo('Digite ultimo numerador: ')
    somatorio = 0
    for numerador in range(1, num_final+1):
        if numerador % 2 == 0:
            print(f'{num_final-(numerador-1)} / {numerador}')
            somatorio -= (numerador/num_final-(numerador-1))
        else:
            print(f'{numerador} / {num_final-(numerador-1)}')
            somatorio += (numerador/num_final-(numerador-1))

    print(f'Somatório: {somatorio:.2f}')
    

main()
