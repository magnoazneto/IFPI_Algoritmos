def main():
    qtd_submissoes = int(input())
    while qtd_submissoes != 0:
        submissoes = []
        for i in range(qtd_submissoes):
            entrada = input().split()
            submissoes.append(entrada)
        qtd_submissoes = int(input())
    

def pontuacao(submissoes):
    aceitos = ''
    for sub in submissoes:
        if sub[2] == 'correct':
            aceitos += sub[0]




# COMO ASSOCIAR OS CORRETOS À QUESTÃO E COMPUTAR OS PONTOS?


main()
