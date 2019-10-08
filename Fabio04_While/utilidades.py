# COMPILADO DE FUNÇÕES SIMPLES E ÚTEIS DE FORMA GERAL 

# Funções matemáticas

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


def valida_opc(opc, msg):
    while opc not in range(1, 3):
        print(msg)
        opc = int(input())
    return opc


def get_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except:
        print('Valor inválido.')
        return get_inteiro(mensagem)


def get_number(mensagem):
    try:
        return float(input(mensagem))
    except:
        print('Valor inválido.')
        return get_number(mensagem)


def get_int_positivo(msg):
    valor = get_inteiro(msg)
    while valor < 0:
        print('Valor digitado menor que 0.')
        valor = get_inteiro(msg)
    return valor


def get_float_positivo(msg):
    valor = get_number(msg)
    while valor < 0:
        print('Valor digitado menor que 0.')
        valor = get_number(msg)
    return valor


def apaga_lista(lista):
    for c in range(0, len(lista)):
        lista.pop()
    return lista


def imprime_lista(lista):
    return ' '.join(map(str, lista))


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


def primo(valor):  # checa se um valor é primo ou não
	total = 0
	for count in range(1, valor+1):
		if valor % count == 0:
			total += 1
	return True if total == 2 else False

def dec2bin(numero):
    if numero > 1:
        resto = str(numero % 2)
        return str(dec2bin(numero//2)) + resto
    else:
        return numero


def dec2hex(numero):
    if numero > 15:
        resto = numero % 16
        resto = filtro_hexadecimal(resto)
        return str(dec2hex(numero//16)) + resto
    else:
        return filtro_hexadecimal(numero)


def filtro_hexadecimal(numero):
    if numero <= 9:
        return str(numero)
    elif numero == 10:
        return 'A'
    elif numero == 11:
        return 'B'
    elif numero == 12:
        return 'C'
    elif numero == 13:
        return 'D'
    elif numero == 14:
        return 'E'
    elif numero == 15:
        return 'F'

def porcentagem(total, qtd):
    return (100*qtd)/total