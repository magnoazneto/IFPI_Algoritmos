from os import system


def cabecalho(msg):
    system('clear')
    print('\n============= '+ msg +' =============')
    print('*' * 27 + '*' * len(msg))


def get_option(msg, begin, end):
    opc = int(input(msg))
    while opc not in range(begin, end):
        print('OPCAO INVALIDA!')
        opc = int(input(msg))
    return opc


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


def get_inteiro(mensagem):  # INT, sem restrição.
    try:
        return int(input(mensagem))
    except ValueError:
        print('Valor inválido.')
        return get_inteiro(mensagem)


def get_number(mensagem):  # FLOAT, sem restrição.
    try:
        return float(input(mensagem))
    except:
        print('Valor inválido.')
        return get_number(mensagem)


def wait():
    input('Pressione qualquer tecla para continuar')
    system('clear')


def fill_with(string, lenght):
    if len(string) < lenght:
        return string + (' '*(lenght - (len(string))))
    else:
        return string



if __name__ == "__main__":
    main()