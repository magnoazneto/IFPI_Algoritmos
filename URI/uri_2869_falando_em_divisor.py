def main():
    for c in range(int(input())):
        divisores_pret = int(input())
        divisores_obtidos = 0
        contador = teste = 1
        while divisores_obtidos < divisores_pret:
            divisores_obtidos = 0
            for c in range(1, teste+1):
                if teste % c == 0:
                    divisores_obtidos += 1
                    if divisores_obtidos == divisores_pret: break
            teste += 1
        print(teste-1)


main()