'''
Compilado de funções matemáticas
'''

def maximo_divisor_comum(num1, num2):
    resto = num1 % num2
    while resto:
        num1 = num2
        num2 = resto
        resto = num1 % num2
    return num2 


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


def fatorial(valor):
    fatorial = 1
    while valor > 0:
        fatorial *= valor
        valor -=1
    return fatorial


def is_prime(num):
    if num > 2 and num % 2 == 0: return False # Fail Fast
    i = 2
    divisores = 2
    while i <= (num ** (1/2)):
        if num % i == 0:
            divisores += 1
        if divisores > 2: break
        i += 1
    if divisores <= 2:
        return True
    else:
        return False
    

def fibonacci(parada): # escreve fibonacci até a 'parada'.
    penultimo = atual = 0
    ultimo = 1
    contador = 3
    print(0, 1, end = ' ')
    while contador <= parada:
        atual = penultimo + ultimo
        print(atual, end = ' ')
        penultimo = ultimo
        ultimo = atual
        contador += 1
    print()


def lista_fibonacci(parada): # escreve fibonacci até a 'parada'.
    fibonacci = [0, 1]
    for c in range(0, parada):
        fibonacci.append(fibonacci[c]+fibonacci[c+1])
    for e in range(0, parada):
        if e != parada-1:
            print(fibonacci[e], end = ' ')
        else:
            print(fibonacci[e])


def maior_valor(num1, num2):
    return num1 if num1 >= num2 else num2


def porcentagem(total, qtd):
    return (100*qtd)/total