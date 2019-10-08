from utilidades import get_inteiro
def main():
    num1 = get_inteiro('Digite o primeiro número: ')
    num2 = get_inteiro('Digite o segundo número: ')
    print(f'MMC: {mmc(num1, num2)}')


def mmc(num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    while True:
        if maior % num1 == 0 and maior % num2 == 0:
            break
        maior += 1
    return maior


main()
