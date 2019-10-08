def main():
    string = input()
    biggest = ''
    while string != '0':
        trab = string.split()
        for i in range(len(trab)):
            if i < len(trab)-1:
                print(len(trab[i]), end='-')
            else:
                print(len(trab[i]))
            if len(trab[i]) >= len(biggest): biggest = trab[i]
        string = input()
    print('\nThe biggest word:', biggest)


main()
