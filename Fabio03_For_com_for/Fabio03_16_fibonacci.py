from get_inputs import get_inteiro
def main():
    qtd = get_inteiro('Digite a quantidade de termos: ')
    penultimo = atual = 0
    ultimo = 1
    print(0, 1, end = ' ')
    for i in range(3, qtd+1):
        atual = penultimo + ultimo
        print(atual, end = ' ')
        penultimo = ultimo
        ultimo = atual
    print()
        

main()