def main():
    for c in range(int(input())):
        string1, string2 = input().split()
        maior = max([len(string1), len(string2)])
        for c in range(0, maior):
            print(imprime_index(string1, c), end = '')
            print(imprime_index(string2, c), end = '')
        print()  


def imprime_index(frase, indice):
    try:
        return frase[indice]
    except:
        return ''


main()