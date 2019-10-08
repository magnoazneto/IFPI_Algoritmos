from os import system
def main():
    matriz = make_array(10)
    acumulador = 0.0
    for i in range(len(matriz)):
        linha = make_array(10)
        for j in range(len(linha)):
            linha[j] = acumulador
            acumulador = ((acumulador*1000) + (150)) / 1000  # adição de 0.15 formatada

        matriz[i] = linha

    show_matrix(matriz)
    
    print('ALGUMAS INFORMAÇÕES SERÃO EXIBIDAS AGORA...')
    wait()
    show_matrix(matriz)
    print('SOMATÓRIO: %.2f' % (soma(matriz)))
    wait()
    show_matrix(matriz)
    print('MÉDIA DAS COLUNAS ÍMPARES: %.2f' % (media_colunas_impares(matriz)))
    wait()
    show_matrix(matriz)
    print('MAIOR VALOR NA DIAGONAL PRINCIPAL: %.2f' % (maior_na_diagonal_principal(matriz)))
    wait()
    print('EXIBINDO VALORES ACIMA DA DIAGONAL PRINCIPAL:')
    acima_diagonal_principal(matriz)
    wait()
    show_matrix(matriz)
    print('\nSOMATÓRIO ABAIXO DA DIAGONAL PRINCIPAL: %.2f' % (somatorio_abaixo_diagonal_principal(matriz)))
    wait()
    numero = get_number('Por favor, informe um número múltiplo de 0.15:\n')
    while (numero*1000) % 150 != 0.0:
        print('Esse número não é múltiplo de 0.15.')
        numero = get_number('Por favor, informe um número múltiplo de 0.15:\n')
    print('A procura pelo número foi concluída: ')
    show_number_in_matrix(matriz, numero)
        

def wait():
    input('Pressione qualquer tecla para continuar')
    system('clear')


def show_number_in_matrix(matriz, numero):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != numero:
                print(str(matriz[i][j]) + '\t', end='')
            else:
                print('[%.2f]\t' % (matriz[i][j]), end = '')
                i_index = i
                j_index = j
        print()
    i = i_index
    j = j_index
    if (i == j) and ((i+j) == len(matriz[i]) - 1):
        print('Número no centro da matriz!')
    if i == j:
        print('Número na diagonal principal.')
    if (i+j) == len(matriz[i]) - 1:
        print('Número na diagonal secundária')
    if j > i:
        print('Acima da diagonal principal')
    elif j < i:
        print('Abaixo da diagonal principal')


def soma(matriz):
    somatorio = 0.0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            somatorio = ((somatorio*1000) + (matriz[i][j]*1000)) / 1000
    
    return somatorio


def media_colunas_impares(matriz):
    somatorio = 0.0
    qtd = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j % 2 != 0:
                somatorio = ((somatorio*1000) + (matriz[i][j]*1000)) / 1000
                qtd += 1
    
    return somatorio / qtd


def maior_na_diagonal_principal(matriz):
    bigger = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == i:
                if matriz[i][j] > bigger:
                    bigger = matriz[i][j]
    
    return bigger


def somatorio_abaixo_diagonal_principal(matriz):
    somatorio = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j < i:
                somatorio = ((somatorio*1000) + (matriz[i][j]*1000)) / 1000

    return somatorio
        

def acima_diagonal_principal(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:
                print(str(matriz[i][j]) + '\t', end='')
            else:
                print((' '* len(str(matriz[i][j]))) + '\t', end = '')
        print()


def show_matrix(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(str(matriz[i][j]) + '\t', end='')
        print()


def make_array(lenght, value=0):
    return [value] * lenght


def transfer(array1, array2):
    for i in range(len(array1)):
        array2[i] = array1[i]


def add_at_last(array, element):
    new_array = make_array(len(array)+1)
    transfer(array, new_array)
    new_array[len(new_array)-1] = element
    return new_array


def get_number(mensagem):  # FLOAT, sem restrição.
    try:
        return float(input(mensagem))
    except:
        print('Valor inválido.')
        return get_number(mensagem)

main()
