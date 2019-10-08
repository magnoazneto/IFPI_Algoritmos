def main():
    for c in range(int(input())):
        string = input()
        quantidade = int(input())
        print(desloca_cesar(string, quantidade))


def desloca_cesar(string, qtd):
    contador = 0
    nova_string = ''
    while contador < len(string):
        codigo = ord(string[contador])
        codigo -= qtd
        if codigo < 65:
            codigo += 26
        nova_string += chr(codigo)
        contador += 1
    return nova_string


main()
