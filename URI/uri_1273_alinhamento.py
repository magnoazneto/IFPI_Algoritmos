def main():
    qtd = int(input())
    while not(qtd == 0):
        palavras = []
        maior = 0
        count = 0
        for c in range(qtd):
            leitura = input()
            if len(leitura) > maior: maior = len(leitura)
            palavras.append(leitura)
        if count == 1:
            print()
        for elemento in palavras:
            if len(elemento) < maior:
                print(elemento.rjust(maior, ' '))
            else:
                print(elemento)
            count += 1
        count = 1
        qtd = int(input())
        if qtd == 0: break


'''
def adapt_word(word, lenght):
    diferenca = lenght - len(word)
    count = 0
    new_str = ''
    while count < diferenca:
        new_str += ' '
        count += 1
    new_str += word
    return new_str '''
        

main()
