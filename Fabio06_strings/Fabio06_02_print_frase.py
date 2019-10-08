def main():
    frase = input('Digite uma frase: ')
    count = 0
    while count < len(frase):
        if frase[count] != ' ':
            print(frase[count], end = '')
        else:
            print(frase[count])
        count += 1
    print()


main()