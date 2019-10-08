def main():
    signature = input()
    codigo = input()
    instance = 1
    while signature != '0':
        print('Instancia %i\nverdadeira' %(instance) if signature in codigo else 'Instancia %i\nfalsa' %(instance))
        signature = input()
        if signature == '0': break
        codigo = input()
        instance += 1
        if instance > 1: print()


main()
