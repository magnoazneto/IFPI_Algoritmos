def main():
    for c in range(0, int(input())):
        qtd1, qtd2 = map(int, input().split()) 
        print(maximo_divisor(qtd1, qtd2))


def maximo_divisor(num1, num2):
    resto = num1 % num2
    while resto:
        num1 = num2
        num2 = resto
        resto = num1 % num2
    return num2 


main()