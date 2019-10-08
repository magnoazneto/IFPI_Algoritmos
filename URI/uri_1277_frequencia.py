def main():
    for cases in range(int(input())):
        estudantes = int(input())
        alunos = input().split()
        frequencia = input().split()
        reprovados = []
        for i in range(estudantes):
            total = len(frequencia[i]) - frequencia[i].count('M')
            presencas = frequencia[i].count('P')
            if percentual(total, presencas) < 75:
                reprovados.append(alunos[i])
        print(' '.join(reprovados))


def percentual(total, qtd):
    return (qtd*100) / total


main()
