from get_inputs import *
def main():
    size = get_int_positivo("Digite o tamanho do vetor: ")
    array = make_array(size)
    print(array)
    for i in range(size):
        array[i] = input("%dº Elemento: " % (i+1))
    reverse = reverse_array(array)
    print(reverse)


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
    
    
def reverse_array(array):
    reverse_array = make_array(len(array))
    for i in range(len(array)-1, -1, -1):    
        add_at_last(reverse_array, array[i])
    return reverse_array


main()
