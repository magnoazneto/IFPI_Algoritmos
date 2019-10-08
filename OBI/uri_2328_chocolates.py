def main():
    cortes = list(map(int, input().split()))
    if len(cortes) != 1:
        pedacos = cortes
        cortes = pedacos[0]
        pedacos = remove_por_index(pedacos, 0)
    else:
        pedacos = list(map(int, input().split()))
    
    print(atualiza_pedacos(pedacos))


def remove_por_index(conjunto, index):
    novo_conjunto = make_array(0)
    for i in range(len(conjunto)):
        if i != index:
            novo_conjunto = add_at_last(novo_conjunto, conjunto[i])
    return novo_conjunto


def atualiza_pedacos(pedacos):
    atuais = 0
    for i in range(len(pedacos)):
        atuais += pedacos[i] - 1

    return atuais    


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