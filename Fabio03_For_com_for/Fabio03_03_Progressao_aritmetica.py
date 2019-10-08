from get_inputs import get_inteiro
def main():
    A0 = get_inteiro('Digite o valor inicial: ')
    limite = get_inteiro('Digite o limite: ')
    razao = get_inteiro('Digite a razão da PA: ')
    progressao_aritmetica(A0, razao, limite)


def progressao_aritmetica(A0, razao, limite):
    if razao == 0:
        print ('Não há progressão se a razão é 0.')
        return 0
    if limite > A0:
        for i in range(A0, limite+1, razao):
            print(i, end = ' ')
    else:
        for i in range(A0, limite-1, razao):
            print(i, end = ' ')
    print()
main()