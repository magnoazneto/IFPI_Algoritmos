def main():
    n = int(input())
    matriz = make_array(n)
    for i in range(n):
        linha = list(map(int, input().split()))
        matriz[i] = linha
    
    print(magic_square(matriz))



def magic_square(matriz):
    magic_number = 0
    for i in range(len(matriz[0])):
        magic_number += matriz[0][i]
    if all_lines(matriz, magic_number):
        if all_collunms(matriz, magic_number):
            if all_diagonals(matriz, magic_number):
                return magic_number
            else:
                return -1
        return -1
    return -1


def all_lines(matrix, magic_number):
    for i in range(len(matrix)):
        somatorio = 0
        for j in range(len(matrix[i])):
            somatorio += matrix[i][j]
        if somatorio != magic_number:
            return False
    
    return True


def all_collunms(matrix, magic_number):
    for i in range(len(matrix)):
        somatorio = 0
        for j in range(len(matrix)):
            somatorio += matrix[j][i]
        if somatorio != magic_number:
            return False
    
    return True


def all_diagonals(matrix, magic_number):
    if principal(matrix, magic_number):
        if secundaria(matrix, magic_number):
            return True
        else:
            return False
    return False


def principal(matrix, magic_number):
    somatorio = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                somatorio += matrix[i][j]
    if somatorio != magic_number:
        return False
    
    return True


def secundaria(matrix, magic_number):
    somatorio = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (i+j) == len(matrix[i]) - 1:
                somatorio += matrix[i][j]
    if somatorio != magic_number:
        return False

    return True


def make_array(lenght, value = 0):
    return [value] * lenght


def transfer(array1, array2):
    for i in range(len(array1)):
        array2[i] = array1[i]


def add_at_last(array, element):
    new_array = make_array(len(array)+1)
    transfer(array, new_array)
    new_array[len(new_array)-1] = element
    return new_array

main()
