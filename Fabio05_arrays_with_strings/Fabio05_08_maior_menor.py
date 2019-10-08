from string_tools import *
def main():
    array = get_number_str('Digite uma sequência de números: ')
    print('Maior número:', get_bigger(array))
    print('Menor número:', get_smaller(array))


def get_smaller(string):
    count = 0
    smaller = 1000
    while count < len(string):
        if int(string[count]) < smaller:
            smaller = int(string[count])
        count += 1
    return smaller


def get_bigger(string):
    count = 0
    bigger = -1000
    while count < len(string):
        if int(string[count]) > bigger:
            bigger = int(string[count])
        count += 1
    return bigger


main()
