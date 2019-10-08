from utilidades import get_number
def main():
    parada = get_number('Digite um número: ')
    print(f'Agora, digite números até que um deles seja igual a {parada}')
    while True:
        valor = get_number('>> ')
        if valor == parada: break
    print('Condição de igualdade atentida!')


main()
