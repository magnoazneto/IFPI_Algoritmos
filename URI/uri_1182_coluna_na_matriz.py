def main():
    #coluna = int(input())
    operacao = input()
    matriz = make_array(12, make_array(12))
    #print(matriz)
    fill_matrix(matriz)
    # for line in matriz:
    #     print(line)
    print("%.1f" % show_results(operacao, matriz))


def show_results(operacao, matriz):
    soma = 0
    qtd = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (j > i) and ((i+j) > len(matriz[i])-1):
                soma += matriz[i][j]
                qtd += 1
    if operacao == 'S':
        return soma
    elif operacao == 'M':
        return soma / qtd


        

'''
def fill_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("Indice [%d][%d]: " % (i, j))
            matrix[i][j] = float(input())
            print(matrix)
'''


def fill_matrix(matrix):
    for i in range(len(matrix)):
        linhas = make_array(len(matrix[i]))
        for j in range(len(linhas)):
            linhas[j] = float(input())
        matrix[i] = linhas
        


def make_array(size, values = 0):
    return [values] * size


def add_at_last(array, element):
    new_array = make_array(len(array) + 1)
    transfer(array, new_array)
    new_array[len(new_array)-1] = element
    array = new_array
    

def transfer(origin, target):
    for i in range(len(origin)):
        target[i] = origin[i]


main()
