# compilado de funções úteis para lidar com strings

def reverse_string(str1): # [::-1]
    count = len(str1) - 1
    reverse_str = ''
    while count >= 0:
        reverse_str += str1[count]
        count -= 1
    return reverse_str

############## CONVERSÕES DE BASE ################

def dec2bin(numero):
    if numero > 1:
        resto = str(numero % 2)
        return str(dec2bin(numero//2)) + resto
    else:
        return numero


def dec2hex(numero):
    if numero > 15:
        resto = numero % 16
        resto = filtro_hexadecimal(resto)
        return str(dec2hex(numero//16)) + resto
    else:
        return filtro_hexadecimal(numero)


def filtro_hexadecimal(numero):
    if numero <= 9:
        return str(numero)
    elif numero == 10:
        return 'A'
    elif numero == 11:
        return 'B'
    elif numero == 12:
        return 'C'
    elif numero == 13:
        return 'D'
    elif numero == 14:
        return 'E'
    elif numero == 15:
        return 'F'

def bin2dec(number): 
    count = 0
    decimal = 0
    number = reverse_string(number)
    while count < len(number):
        decimal += int(number[count]) * (2**count)
        count += 1
    return decimal

#############################################################

def equality_char(string): # verifica se existem elementos repetidos na string
    count = 0
    count2 = 0
    string_aux = string
    equality = 0
    while count < len(string):
        while count2 < len(string):
            if string[count] == string_aux[count2]:
                equality += 1
                if equality == 2: return True
            count2 += 1
        count += 1
        count2 = 0
        equality = 0
    return False


def substring(string, inicio, fim): # devolve uma substring entre os índices
    nova_string = ''
    while inicio < fim:
        nova_string += string[inicio]
        inicio += 1
    return nova_string


def its_in(string, piece, begin= 0): # IN
    if len(piece) > len(string): return False  # Fail fast
    len_substring = len(piece)
    limit = len(string) - len(piece)
    while begin <= limit:
        if substring(string, begin, begin + len_substring) == piece:
            return True
        begin += 1
    return False


def get_binary(msg):  # input restrita para números binários.
    binary = input(msg)
    while binary_check(binary) == False:
        print('Isso não é binário.')
        binary = input(msg)
    return binary


def get_string(lenght, msg):  # input com restrição de tamanho na string
    string = input(msg)
    while len(string) != lenght:
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


def number_check(string):  # checa se uma string é formada apenas por números
    count = 0
    while count < len(string):
        if ord(string[count]) < 48 or ord(string[count]) > 57:
            return False
        count += 1
    return True


def get_smaller(string):  # menor valor
    count = 0
    smaller = 1000
    while count < len(string):
        if int(string[count]) < smaller:
            smaller = int(string[count])
        count += 1
    return smaller


def get_bigger(string):  # maior valor
    count = 0
    bigger = -1000
    while count < len(string):
        if int(string[count]) > bigger:
            bigger = int(string[count])
        count += 1
    return bigger


def sort_string(string):  # ordena uma string buscando os maiores valores
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


def string_pop(string, index):  # remove um elemento da string pelo índice
    count = 0
    new_str = ''
    while count < len(string):
        if count != index:
            new_str += string[count]
        count += 1
    return new_str


def get_bigger_and_index(string):  # maior valor e o índice
    count = 0
    bigger = -1000
    index = 0
    while count < len(string):
        if int(string[count]) > bigger:
            bigger = int(string[count])
            index = count
        count += 1
    return bigger, index