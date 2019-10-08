def main():
    valor1 = valor2 = 1
    while valor1 > 0 and valor2 > 0:
        valor1, valor2 = map(int, input().split())
        somatorio = 0
        if valor1 <= 0 or valor2 <= 0:
            break
        for c in range(min([valor1, valor2]), max([valor1, valor2])+1):
            print(c, end=' ')
            somatorio += c
        print('Sum={}'.format(somatorio))


main()