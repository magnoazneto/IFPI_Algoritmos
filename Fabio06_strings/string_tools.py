# compilado de funções úteis para lidar com strings

def reverse_string(str1): # [::-1]
    count = len(str1) - 1
    reverse_str = ''
    while count >= 0:
        reverse_str += str1[count]
        count -= 1
    return reverse_str

############## CONVERSÕES DE BASE ################

def dec2bin(numero): # decimal para binário
    if numero > 1:
        resto = str(numero % 2)
        return str(dec2bin(numero//2)) + resto
    else:
        return numero


def dec2hex(numero): # decimal para hexadecimal
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

def bin2dec(number): # binário para decimal
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


def substring(string, inicio, fim):  # devolve uma substring entre os índices
    nova_string = ''
    while inicio < fim:
        nova_string += string[inicio]
        inicio += 1
    return nova_string


def its_in(string, piece, begin= 0):  # simula o IN
    if len(piece) > len(string): return False  # Fail fast
    len_substring = len(piece)
    limit = len(string) - len(piece)
    while begin <= limit:
        if substring(string, begin, begin + len_substring) == piece:
            return True
        begin += 1
    return False


def found_it(string, piece, begin= 0):  # devolve o primeiro index de uma substring dentro de outra
    if len(piece) > len(string): return False  # Fail fast
    len_substring = len(piece)
    limit = len(string) - len(piece)
    while begin <= limit:
        if substring(string, begin, begin + len_substring) == piece:
            return begin
        begin += 1
    return False


def number_check(string):  # checa se uma string é formada apenas por números
    count = 0
    while count < len(string):
        if ord(string[count]) < 48 or ord(string[count]) > 57:
            return False
        count += 1
    return True


def get_smaller(string):  # menor valor de uma string numerica
    count = 0
    smaller = 1000
    while count < len(string):
        if int(string[count]) < smaller:
            smaller = int(string[count])
        count += 1
    return smaller


def get_bigger(string):  # maior valor de uma string numerica
    count = 0
    bigger = -1000
    while count < len(string):
        if int(string[count]) > bigger:
            bigger = int(string[count])
        count += 1
    return bigger


def sort_string(string):  # ordena uma string numerica buscando os maiores valores
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


def remove_all(string, remove_char):  # remove todas as ocorrências de um char numa string
    count = 0
    new_str = ''
    while count < len(string):
        if string[count] != remove_char:
            new_str += string[count]
        count += 1
    return new_str


def is_palindrome(word):  # verifica se uma paravra é um palíndromo
    return True if word == reverse_string(word) else False


def lower(word):  # torna todas as letras de uma string minusculas
    count = 0
    new_str = ''
    while count < len(word):
        if is_letter(word[count]):
            codigo = ord(word[count])
            if codigo >= 65 and codigo <= 90:
                new_str += chr(codigo + 32)
            else:
                new_str += word[count]
        else:
            new_str += word[count]
        count += 1
    return new_str


def upper(word):  # torna todas as letras de uma string maiusculas
    count = 0
    new_str = ''
    while count < len(word):
        if is_letter(word[count]):
            codigo = ord(word[count])
            if codigo >= 97 and codigo <= 122:
                new_str += chr(codigo - 32)
            else:
                new_str += word[count]
        else:
            new_str += word[count]
        count += 1
    return new_str


def is_letter(char):  # checa se o caractere é uma letra
    codigo = ord(char)
    if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
        return True
    else:
        return False


def strip_str(text):  # corta todos os espaços extras de uma string
    if len(text) == 0: return ''
    previous_space = True
    count = 0
    new_str = ''
    while count < len(text):
        if (not previous_space or text[count] != ' '):
            new_str += text[count]
            if text[count] == ' ': 
                previous_space = True
            else:
                previous_space = False
        count +=1
    if len(new_str) > 0 and new_str[-1] == ' ': 
        new_str = string_pop(new_str, len(new_str)-1)   
    return new_str


def bigger_substr(str_min, str_max):  # retorna o tamanho da maior substring comum entre 2 strings
    if str_min > str_max:
        str_min, str_max = str_max, str_min
    if str_min in str_max: return len(str_min)
    start = 0
    loop = 1
    extension = len(str_min) - loop
    while loop <= len(str_min):
        while start <= loop:
            sub_str = str_min[start:extension+start]
            if sub_str in str_max: return len(sub_str)
            start += 1
        loop += 1
        extension -= 1
        start = 0
    return 0


def in_ordered(string, sub_str, begin= 0):  # simula o IN, mas olhando apenas a ordem dos caracteres
    if len(sub_str) > len(string): return False  # Fail fast
    sub_str_index = 0
    tester = ''
    while begin < len(string):
        if sub_str[sub_str_index] == string[begin]:
            tester += string[begin]
            sub_str_index += 1
            if sub_str == tester: return True
        begin += 1
    return False


def is_uppercase(char):  # checa se um caractere é UPPERCASE
    return ord(char) >= 65 and ord(char) <= 90


def is_lowercase(char):  # checa se um caractere é lowercase
    return ord(char) >= 97 and ord(char) <= 122


def replace_all(string, target, piece):  # substitui todas as ocorrencias do target por piece
    i = 0
    new_str = ''
    limit = len(string) - len(target)
    while i < len(string):
        if i <= limit and substring(string, i, i+len(target)) == target:
            new_str += piece
            i += len(target) - 1
        else:
            new_str += string[i]
        i += 1
    return new_str


def replace_first(string, target, piece):  # substitui a primeira ocorreira do target por piece
    index = found_it(string, target)
    if not(index): return 'Não há alvo a ser retirado.' 
    i = 0
    new_str = ''
    while i < len(string):
        if i != index:
            new_str += string[i]
        else:
            new_str += piece
            i += len(target) - 1
        i += 1
    return new_str 


def apaga_lista(lista):  # Deixa uma lista vazia
    for c in range(0, len(lista)):
        lista.pop()
    return lista


def imprime_lista(lista):  # Imprime uma lista no formato STR
    return ' '.join(map(str, lista))