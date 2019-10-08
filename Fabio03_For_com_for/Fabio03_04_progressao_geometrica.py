from get_inputs import get_inteiro
def main():
    A0 = get_inteiro('Digite o valor inicial: ')
    limite = get_inteiro('Digite o limite: ')
    razao = get_inteiro('Digite a razão da PA: ')
    progressao_geometrica(A0, razao, limite)

'''
 Não é interessante colocar um for nesse caso,
 porque o for de python não suporta "i *= razão"
'''
# porém deu pra fazer em Javascript :)

def progressao_geometrica(A0, razao, limite):
    while A0 <= limite:
        print(A0, end = ' ')
        A0 *= razao
    print()
main()