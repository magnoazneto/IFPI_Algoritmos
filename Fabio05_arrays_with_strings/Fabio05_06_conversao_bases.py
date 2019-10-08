from string_tools import reverse_string
def main():
    try:
        binary = get_binary('Digite um número binário com 2 nibbles: ')
        print('Binário: %s' %(binary))
        decimal = bin2dec(binary)
        print('Decimal: %i' %(decimal))
        print('Hexadecimal: %s' %(dec2hex(decimal)))
    except:
        print('\nTchau!')


def bin2dec(number):
    count = 0
    decimal = 0
    number = reverse_string(number)
    while count < len(number):
        decimal += int(number[count]) * (2**count)
        count += 1
    return decimal


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


def get_binary(msg):
    binary = get_string(8, msg)
    while binary_check(binary) == False:
        print('Isso não é binário.')
        binary = get_string(8, msg)
    return binary


def get_string(lenght, msg):
    string = input(msg)
    while len(string) != lenght:
        print('Tamanho incorreto. Você digitou %i elementos.' %(len(string)))
        string = input(msg)
    return string


def binary_check(binary):
    count = 0
    while count < len(binary):
        if not(binary[count] == '0' or binary[count] == '1'):
            return False
        count += 1
    return True


main()
