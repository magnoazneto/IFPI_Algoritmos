from utilidades import get_number, get_int_positivo
def main():
    prova = 1
    nadadores = 1
    clubeA = clubeB = 0
    while not(prova == 0 and nadadores == 0):
        prova = get_int_positivo('Nª da prova: ')
        nadadores = get_int_positivo('Qtd de nadadores: ')
        if nadadores == 0 and prova == 0: break
        contador = 1
        while contador <= nadadores:
            print(f'{contador}º nadador:')
            nome = input('Nome: ')
            classificacao = get_int_positivo('Classificação: ')
            tempo = get_number('Tempo: ')
            clube = valida_clube('Clube: ')
            if clube == 'a':
                clubeA += pontuacao(classificacao)
            else:
                clubeB += pontuacao(classificacao)
            contador += 1
        print('=='*10)
        print(f'Prova Nº {prova}')
        print(f'Clube A: {clubeA} pontos')
        print(f'Clube B: {clubeB} pontos')
        print(vencedor(clubeA, clubeB))


def vencedor(clubeA, clubeB):
    if clubeA > clubeB:
        return 'Clube A venceu!'
    elif clubeA == clubeB:
        return 'Empate!'
    else:
        return 'Clube B venceu!'


def valida_clube(msg):
    while True:
        clube = input(msg)
        if clube == 'a' or clube == 'b':
            return clube
        else:
            print('Clube inválido')


def pontuacao(classificacao):
    if classificacao == 1:
        return 9
    elif classificacao == 2:
        return 6
    elif classificacao == 3:
        return 4
    elif classificacao == 4:
        return 3
    else:
        return 0


main()
