from string_tools import substring
def main():
    verbo = input('Digite um verbo terminado em ER: ')
    conjuga_verbo(verbo)


def conjuga_verbo(verbo):
    if substring(verbo, len(verbo)-2, len(verbo)) == 'er':
        radical = substring(verbo, 0, len(verbo)-2)
    else:
        print('Esse verbo não termina em ER.')
        return 0
    print('Eu %so' %radical)
    print('Tu %ses' %radical)
    print('Ele/Ela %se' %radical)
    print('Nós %semos' %radical)
    print('Vós %seis' %radical)
    print('Eles/Elas %sem' %radical)



main()
