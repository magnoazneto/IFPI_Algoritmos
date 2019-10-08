def main():
    for c in range(0, int(input())):
        qtd1, qtd2 = map(int, input().split()) 
        print(maximo_divisor(qtd1, qtd2))


def maximo_divisor(qtd1, qtd2):
    for c in range(menor_valor(qtd1, qtd2), 0, -1):
        if qtd1 % c == 0 and qtd2 % c == 0:
            return c


def menor_valor(num1, num2):
    return num1 if num1 <= num2 else num2
    

main()           
