from get_inputs import get_int_zeromaior
def main():
    print('Esse programa exibe uma das 4 tabuadas.')
    print('Selecione a tabuada desejada:')
    print('1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\n')
    opc = get_opc('>> ')
    if opc == 1:
        adicao()
    elif opc == 2:
        subtracao()
    elif opc == 3:
        multiplicacao()
    else:
        divisao()
    

def multiplicacao():
    for numero in range(1, 11):
        for contador in range(1, 11):
            print('{} x {} = {}'.format(numero, contador,\
                                         numero*contador))    
        print('=====================')


def adicao():
    for n in range(1, 11):
        for c in range(1, 11):
            print('%d + %d = %d' %(n, c, n+c))
        print('=====================')

    
def subtracao():
    for n in range(1, 11):
        for c in range(0, 10):
            print('%d - %d = %d' %(n+c, n, c))
        print('=====================')


def divisao():
    for n in range(1, 11):
        for c in range(1, 11):
            print('%d / %d = %d' %(c*n, n, c))
        print('=====================')


def get_opc(msg):
    opc = get_int_zeromaior(msg)
    while opc not in range(1,5):
        print('Opção inválida')
        opc = get_int_zeromaior(msg)
    return opc

        

main()