def main():
    for c in range(0, int(input())):
        mina = list(input())
        print(remove_diamante(mina))


def remove_diamante(mina):
    esquerda = 0
    diamantes = 0
    for c in range(0, len(mina)):
        if mina[c] == '<':
            esquerda = True
        else:
            esquerda = False
        if esquerda == True:
            for d in range(c, len(mina)):
                if mina[d] == '>':
                    mina[d] = mina[c]= 'retirado'
                    diamantes += 1
                    esquerda = False
                    break
    return diamantes


main()
