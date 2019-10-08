
def main():
    while True:
        try:
            a, b = map(int, input().split())
            print(a ^ b)
            #print('Resultado da minha função: ')
            #print(xor(a, b))

        except EOFError:
            break


def xor(a, b):
    bin_a = fill_with(dec2bin(a), '0', 32)
    bin_b = fill_with(dec2bin(b), '0', 32)
    result = ''
    for i in range(32):
        if bin_a[i] != bin_b[i]:
            result += '1'
        else:
            result += '0'
    
    return bin2dec(result)
    

def bin2dec(number): # binário para decimal
    count = 0
    decimal = 0
    number = number[::-1]
    while count < len(number):
        decimal += int(number[count]) * (2**count)
        count += 1
    return decimal


def fill_with(string, char, lenght):
    result = ''
    for _ in range(0, lenght - (len(string))):
        result += char
    return (result + string)


def dec2bin(numero): # decimal para binário
    if numero > 1:
        resto = str(numero % 2)
        return str(dec2bin(numero//2)) + resto
    else:
        return numero


main()
