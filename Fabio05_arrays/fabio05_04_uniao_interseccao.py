def main():
    lenght = int(input("Digite o tamanho N: "))
    vetor_a = make_array(lenght)
    vetor_b = make_array(lenght)
    print("Quais os valores de A?\n")
    fill_array(vetor_a)
    print("Quais os valores de B?\n")
    fill_array(vetor_b)
    vetor_uniao = uniao(list(set(vetor_a)), list(set(vetor_b)))
    vetor_intersecao = intersecao(list(set(vetor_a)), list(set(vetor_b)))
    print(vetor_uniao)
    print(vetor_intersecao)


def uniao(array1, array2):
    union = make_array(0)
    transfer(array1, union)
    for i in range(len(array2)):
        if not my_in(array2[i], union):
            union += [array2[i]]
    return union


def intersecao(array1, array2):
    intersection = make_array(0)
    for i in range(len(array1)):
        if my_in(array1[i], array2):
            intersection += [array1[i]]
    return intersection


def my_in(piece, target):
    for i in range(len(target)):
        if piece == target[i]:
            return True

    return False


def transfer(array, target):
    for i in range(len(array)):
        target += [array[i]]


def make_array(lenght, value=0):
    return [value] * lenght


def fill_array(array):
    for i in range(len(array)):
        array[i] = int(input('%dº item: ' % (i+1)))


main()
