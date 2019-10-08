from utilidades import get_inteiro
def main():
    A0 = get_inteiro('Digite o valor inicial: ')
    limite = get_inteiro('Digite o limite: ')
    razao = get_inteiro('Digite a razão da PA: ')
    progressao_geometrica(A0, razao, limite)


def progressao_geometrica(A0, razao, limite):
    while A0 <= limite:
        print(A0, end = ' ')
        A0 *= razao
    print()
main()