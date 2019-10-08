def main():
    contador = 1
    casos = int(input())
    while contador <= casos:
        texto = input()
        texto = deslocamento_letra(texto, 3)
        texto = inverte_string(texto)
        texto = texto[0:len(texto)//2] + desloca_char(texto[len(texto)//2:], -1)
        print(texto)
        contador += 1


def desloca_char(texto, qtd):
    contador = 0
    nova_string = ''
    while contador < len(texto):
        codigo = ord(texto[contador])
        codigo += qtd
        nova_string += chr(codigo)
        contador += 1
    return nova_string


def deslocamento_letra(texto, qtd):
    contador = 0
    nova_string = ''
    while contador < len(texto):
        if texto[contador].isalpha():
            nova_string += desloca_char(texto[contador], 3)
        else:
            nova_string += texto[contador]
        contador += 1
    return nova_string


def inverte_string(texto):
    contador = len(texto) - 1
    nova_string = ''
    while contador >= 0:
        nova_string += texto[contador]
        contador -= 1
    return nova_string


main()