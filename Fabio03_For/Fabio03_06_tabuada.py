def main():
    numero = 1
    contador = 1
    while numero <= 10:
        while contador <= 10:
            print('{} x {} = {}'.format(numero, contador,\
                                         numero*contador))
            contador += 1
        print('='*15)
        numero += 1
        contador = 1
        

main()