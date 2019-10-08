def main():
    alunos = int(input('Quantos alunos existem na classe? '))
    atividades = int(input('Quantas atividades cada aluno realizou? '))
    rendimento(alunos, atividades)


def rendimento(alunos, atividades):
    i = 1
    aprovados = ''
    ap_count = 0
    reprovados = ''
    rp_count = 0
    while i <= alunos:
        nome = input(f'Nome do {i}º aluno: ')
        c = 1
        media = 0
        media_turma = 0
        nota = 0
        acumulador_peso = 0
        while c <= atividades:
            nota = float(input(f'Nota da {c}ª atividade: '))
            peso = float(input(f'Peso desta atividade: '))
            acumulador_peso += peso
            media += nota * peso
            c += 1
        media = media / acumulador_peso
        media_turma += media
        if media >= 7:
            aprovados += nome + ' ' + str(media) + '\n'
            ap_count += 1
        else:
            reprovados += nome + ' ' + str(media) + '\n'
            rp_count += 1
        i += 1
    print(f'{ap_count} alunos foram aprovados.\n{rp_count} alunos foram reprovados.')
    print(f'Média da turma: {media_turma:.1f}')
    print('Aprovados:\n', aprovados, sep = '')
    print('==================================')
    print('Reprovados:\n', reprovados, sep = '')


main()
