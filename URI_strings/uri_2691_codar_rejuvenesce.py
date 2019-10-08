def main():
    for c in range(int(input())):
        inicio, fim = map(int, input().split())
        for c in range(inicio, fim+1):
            print(c, end = '')
        for c in range(fim, inicio-1, -1):
            print(inverte_string(str(c)), end= '')
        print()


def inverte_string(string):
    contador = len(string) - 1
    nova_string = ''
    while contador >= 0:
        nova_string += string[contador]
        contador -= 1
    return nova_string


main()
