"""
Questão resolvida usando listas e dicionários.
Uma possível solução sem usar essas ferramentas seria:
1. Criar uma função que simule o count() de listas, mas para strings;
2. No lugar do append na lista 'letras', usar concatenação;
3. Criar um 'for i in range(97, 123)' para percorrer cada uma das letras do alfabeto;
4. Dentro desse for, verificar a quantidade de letras em cada iteração com a função feita
    no passo 1, e printar o resultado de cada letra.

Porém, nesse caso a identificação das 5 letras que menos aparecem nas palavras do arquivo
aconteceria de forma visual, observando a quantidade de ocorrências de todas as 26 letras
do alfabeto.
"""

from string_list_tools import its_in
def main():
    fin = open('words.txt')
    letras = []
    for line in fin:
        word = remove_duplicated(line)
        for i in range(0, len(word)):
            letras.append(word[i])
    #print(letras)
    conta_repetidos(letras)
    

def conta_repetidos(lista):
    contagem = {}
    for codigo in range(97, 123):
        char = chr(codigo)
        print(f'Letra {char}: {lista.count(char)}')
        contagem.update({char:(lista.count(char))})
    #print(contagem)
    organizado = sorted(contagem, key= contagem.get)
    print('Combinação de 5 letras que menos aparecem:')
    for c in range(0, 5):
        print(organizado[c], end=' ')
    print()


def remove_duplicated(string):  # remove todos os elementos duplicados em uma string
    new_str = ''
    for i in range(0, len(string)-1):
        if not its_in(new_str, string[i]):
            new_str += string[i]
    return new_str


if __name__ == '__main__':
    main()
