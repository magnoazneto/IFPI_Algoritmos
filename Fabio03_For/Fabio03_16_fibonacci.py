from utilidades import get_inteiro
def main():
    qtd = get_inteiro('Digite a quantidade de termos: ')
    penultimo = atual = 0
    ultimo = 1
    contador = 3
    print(0, 1, end = ' ')
    while contador <= qtd:
        atual = penultimo + ultimo
        print(atual, end = ' ')
        penultimo = ultimo
        ultimo = atual
        contador += 1
    print()
        

main()