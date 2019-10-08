def main():
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    print(mdc(n1, n2))


def mdc(n1, n2):
    resto = 1
    while resto:
        resto = n1 % n2
        n1 = n2
        n2 = resto
    return n1



main()
