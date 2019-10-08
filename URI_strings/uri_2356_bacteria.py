def main():
    while True:
        try:
            D = input()
            print('Resistente' if input() in D else 'Nao resistente')
        except EOFError:
            break
        


main()