def main():
    pares = impares = positivos = negativos = 0
    for c in range(0, 5):
        valor = int(input())
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1
        if valor >= 0:
            if valor != 0:
                positivos += 1
            else:
                pass
        else:
            negativos += 1

    print('{} valor(es) par(es)'.format(pares))
    print('{} valor(es) impar(es)'.format(impares))
    print('{} valor(es) positivo(s)'.format(positivos))
    print('{} valor(es) negativo(s)'.format(negativos))


main()