def main():
    alvo = int(input())
    operacao = input()
    matriz = []
    linhas = []
    soma = 0
    for linha in range(0, 12):
        for coluna in range(0, 12):
            linhas.append(float(input()))
        matriz.append(linhas)
        linhas = []
    if operacao == 'S':
        for i in range(0, len(matriz)):
            soma += matriz[i][alvo]
        print(f'{soma:.1f}')
    elif operacao == 'M':
        for i in range(0, len(matriz)):
            soma += matriz[i][alvo]
        print(f'{soma/len(matriz):.1f}')
        

main()
