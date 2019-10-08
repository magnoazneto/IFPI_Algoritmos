'''
Compilado de funções usadas para receber
dados de forma restrita.
'''

def get_inteiro(mensagem):  # INT, sem restrição.
    try:
        return int(input(mensagem))
    except:
        print('Valor inválido.')
        return get_inteiro(mensagem)


def get_number(mensagem):  # FLOAT, sem restrição.
    try:
        return float(input(mensagem))
    except:
        print('Valor inválido.')
        return get_number(mensagem)


def get_int_zeromaior(msg):  # INT >= 0
    valor = get_inteiro(msg)
    while valor < 0:
        print('Valor digitado menor que 0.')
        valor = get_inteiro(msg)
    return valor


def get_float_zeromaior(msg):  # FLOAT >= 0
    valor = get_number(msg)
    while valor < 0:
        print('Valor digitado menor que 0.')
        valor = get_number(msg)
    return valor


def get_string(lenght, msg):  # input com restrição de tamanho na string
    string = input(msg)
    while len(string) != lenght:
        print('Tamanho incorreto. Você digitou %i elementos.' %(len(string)))
        string = input(msg)
    return string


def get_string_max(lenght, msg):  # input com restrição de tamanho max na string
    string = input(msg)
    while len(string) > lenght:
        print('Tamanho incorreto. Você digitou %i elementos.' %(len(string)))
        string = input(msg)
    return string


def binary_check(binary):  # checa se uma string corresponde a um número binário
    count = 0
    while count < len(binary):
        if not(binary[count] == '0' or binary[count] == '1'):
            return False
        count += 1
    return True


def get_number_str(msg):  # input restrito para strings de números
    number_str = input(msg)
    while number_check(number_str) == False:
        print('A string deve conter apenas números.')
        number_str = input(msg)
    return number_str