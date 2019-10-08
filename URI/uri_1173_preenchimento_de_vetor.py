def main():
    lista = []
    for c in range(0, 100):
        lista.append(float(input()))
    for c in range(0, 100):
        if lista[c] <= 10:
            print('A[%d] = %.1f' %(c, lista[c]))


main()
