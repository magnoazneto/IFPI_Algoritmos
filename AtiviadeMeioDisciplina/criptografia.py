def main():
    frase = input()
    cripted_frase = cripto_frase(frase)
    print(cripted_frase)
    print_changes(cripted_frase)
    

def cripto_frase(string):
    frase = trata_vogais(string)
    frase = trata_cases(frase)
    frase = trata_numeros(frase)
   # frase = desloca_frase(frase)
    return frase


def print_changes(string):
    letras = 0
    numerais = 0
    especiais = 0
    demais = 0
    i = 0
    while i < len(string):
        if is_letter(string[i]):
            letras += 1
        elif is_number(string[i]):
            numerais += 1
        elif ord(string[i]) >= 33 and ord(string[i]) <= 47:
            especiais += 1
        else:
            demais += 1
        i += 1
    print('Letras:', letras)
    print('Numerais:', numerais)
    print('Especiais:', especiais)
    print('Demais:', demais)


def desloca_frase(string, step = 5):
    i = 0
    new_str = ''
    while i < len(string):
        new_str += chr(ord(string[i]) + step)
        i += 1
    return new_str


def trata_cases(string):
    i = 0
    new_str = ''
    while i < len(string):
        if is_letter(string[i]):
            if is_upper(string[i]):
                new_str += chr(ord(string[i]) + 32)
            else:
                new_str += chr(ord(string[i]) - 32)
        else:
            new_str += string[i]
        i += 1
    return new_str


def trata_numeros(string):
    i = 0
    number = 0
    new_str = ''
    while i < len(string):
        if is_number(string[i]):
            number = int(string[i]) ** 2
            if len(str(number)) > 1:
                new_str += comprime_numero(number)
            else:
                new_str += str(number)
        else:
            new_str += string[i]
        i += 1
    return new_str


def comprime_numero(number):
    i = 0
    pocket = ''
    number = str(number)
    while i < len(number):
        pocket += number[i]
        i += 1
    return pocket
        

def trata_vogais(string):
    i = 0
    new_str = ''
    while i < len(string):
        if is_letter(string[i]):
            if string[i] == 'a':
                new_str += 'u'
            elif string[i] == 'e':
                new_str += 'o'
            elif string[i] == 'o':
                new_str += 'e'
            elif string[i] == 'u':
                new_str += 'a'
            elif string[i] == 'A':
                new_str += 'U'
            elif string[i] == 'E':
                new_str += 'O'
            elif string[i] == 'O':
                new_str += 'E'
            elif string[i] == 'U':
                new_str += 'A'
            else:
                new_str += string[i]
        else:
            new_str += string[i]
        i += 1
    return new_str



def is_upper(char):
    return ord(char) >= 65 and ord(char) <= 90


def is_letter(char):
    return ord(char) >= 65 and ord(char) <= 90 or ord(char) >= 97 and ord(char) <= 122


def is_number(char):
    return ord(char) >= 48 and ord(char) <= 57


main()
