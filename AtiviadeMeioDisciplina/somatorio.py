def main():
    print('Esse script verificará todos os números perfeitos entre N e M.')
    n = int(input('Digite o valor de N: '))
    m = int(input('Digite o valor de M: '))
    serie_perfeita_recursiva(n, m)


def serie_perfeita(begin, end):
    if end < begin: 
        print('M é menor que N. Não há sequência.')
        return 0
    while begin <= end:
        if is_perfect(begin):
            print('Número perfeito:', begin)
        begin += 1


def is_perfect(number):
    i = 1
    somatorio = 0
    while i < number:
        if number % i == 0:
            somatorio += i
        i += 1
    if somatorio == number:
        return True
    else:
        return False

    
def serie_perfeita_recursiva(begin, end):
    if end < begin:
        print('M é menor que N. Fim da sequência.')
        return 0
    else:
        if is_perfect(begin):
            print('Número perfeito:', begin)
        else:
            print('Número não perfeito:', begin)
    serie_perfeita_recursiva(begin + 1, end)
            


main()
