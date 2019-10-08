from utilidades import get_inteiro
def main():
    decimal = get_inteiro('Digite um número inteiro: ')
    print(f'Romano: {dec2roman(decimal)}')


def dec2roman(decimal):
    if decimal >= 500:
        return 'D' + dec2roman(decimal-500)
    elif decimal >= 100:
        return 'C' + dec2roman(decimal-100)
    elif decimal >= 50:
        return 'L' + dec2roman(decimal-50)
    elif decimal >= 10:
        return 'X' + dec2roman(decimal-10)
    elif decimal >= 5:
        return 'V' + dec2roman(decimal-5)
    elif 


main()
