from utilidades import get_int_positivo
def main():
    serra = dilma = ciro = indecisos = outros = branulos = 0
    total = 0
    mensagem = 'Em quem você pretende votar nas \
eleições?\n45-Serra\n13-Dilma\n23-Ciro\n99-Indeciso\n98-Outros\
\n00-Nulo/Branco\n>> '
    opiniao = valida_opiniao(mensagem)
    while opiniao != 1:
        if opiniao == 45:
            serra += 1
            total += 1
        elif opiniao == 13:
            dilma += 1
            total += 1
        elif opiniao == 23:
            ciro += 1
            total += 1
        elif opiniao == 99:
            indecisos += 1
            total += 1
        elif opiniao == 98:
            outros += 1
            total += 1
        elif opiniao == 0:
            branulos += 1
            total += 1
        opiniao = valida_opiniao(mensagem)
    print('==='*15)
    print('Intenções de voto:')
    print(f'Serra: {porcentagem(total, serra):.1f} %')
    print(f'Dilma: {porcentagem(total, dilma):.1f} %')
    print(f'Ciro: {porcentagem(total, ciro):.1f} %')
    print(f'Outros: {porcentagem(total, outros):.1f} %')
    print(f'Indecisos: {porcentagem(total, indecisos):.1f} %')
    print(f'Brancos/Nulos: {porcentagem(total, branulos):.1f} %')
    print(f'{total} pessoas foram entrevistadas!')
    if serra == dilma and (ciro < serra and ciro < dilma):
        print('Possibilidade de segundo turno: Serra x Dilma!')
    elif serra == ciro and (dilma < serra and dilma < ciro):
        print('Possibilidade de segundo turno: Serra x Ciro!')
    elif dilma == ciro and (serra < dilma and serra < ciro):
        print('Possibilidade de segundo turno: Dilma x Ciro!')
    elif dilma == ciro == serra:
        print('Segundo turno entre os três!')


def porcentagem(total, qtd):
    return (100*qtd)/total


def valida_opiniao(msg):
    while True:
        opiniao = get_int_positivo(msg)
        if opiniao == 45 or opiniao == 13 or opiniao == 23\
            or opiniao == 99 or opiniao == 98 or opiniao == 0\
            or opiniao == 1:
            return opiniao
        else:
            print('Opinião inválida.')


main()