from utilidades import get_number
def main():
    parada = get_number('Digite um número: ')
    anterior = 0
    print(f'Agora, digite números até que a soma de dois\
 deles seja igual a {parada}')
    while True:
        valor = get_number('>> ')
        if (valor + anterior) == parada: break
        anterior = valor
    print('Condição de igualdade atentida!')


main()
