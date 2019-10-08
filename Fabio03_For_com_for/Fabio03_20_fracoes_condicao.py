from get_inputs import get_int_positivo
def main():
    den_final = get_int_positivo('Digite o ultimo denominador: ')
    somatorio = 0
    for denominador in range(1, den_final+1):
        if denominador % 2 != 0:
            somatorio += (1/denominador)
        else:
            somatorio -= (1/denominador)
    print(f'Somatório: {somatorio:.2f}')
    

main()
