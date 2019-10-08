def main():
    for c in range(0, int(input())):
        circulo, salto = map(int, input().split())
        print('Case {}: {}'.format(c+1, sobrevivente(circulo, salto)))



def sobrevivente(circulo, salto):
    pessoas = []
    for c in range(1, circulo+1):
        pessoas.append(c)
    mortos = pessoas.count('Morto')
    while mortos < (len(pessoas)-1):
        for c in range(0, len(pessoas)-1, salto):
            if pessoas[c] != 'Morto':
                pessoas[c] = 'Morto'
        while 'Morto' in pessoas:
            pessoas.remove('Morto')
    
    return pessoas[0] 


main()