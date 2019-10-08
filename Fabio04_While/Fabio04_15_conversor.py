from utilidades import get_int_positivo
def main():
    decimal = valida_dec('Digite um número decimal: ')
    print(f'Binário: {dec2bin(decimal)}')
    print(f'Hexadecimal: {dec2hex(decimal)}')


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


def valida_dec(msg):
    while True:
        decimal = get_int_positivo(msg)
        if decimal > 255:
            print('Número deve ser menor que 256.')
        else:
            return decimal


main()
