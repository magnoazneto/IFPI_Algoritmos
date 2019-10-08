from string_tools import reverse_string, get_number_str
def main():
    array = get_number_str('Digite uma sequencia de valores para ordenação: ')
    new_array = sort_string(array)
    print('String ordenada:', new_array)


def sort_string(string):
    bigger = -1000
    count = 0
    sorted_string = ''
    index = 0
    limit = len(string)
    while count < limit:
        bigger, index = get_bigger_and_index(string)
        sorted_string = str(bigger) + sorted_string
        string = string_pop(string, index)
        count += 1
    return sorted_string


def string_pop(string, index):
    count = 0
    new_str = ''
    while count < len(string):
        if count != index:
            new_str += string[count]
        count += 1
    return new_str


def get_bigger_and_index(string):  # maior valor e o indice
    count = 0
    bigger = -1000
    index = 0
    while count < len(string):
        if int(string[count]) > bigger:
            bigger = int(string[count])
            index = count
        count += 1
    return bigger, index


main()
