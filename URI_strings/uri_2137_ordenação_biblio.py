def main():
    prateleira = []
    while True:
        try:
            prateleira = []
            for c in range(int(input())):
                prateleira.append(input())
                prateleira.sort()
            for c in prateleira:
                    print(c)

        except EOFError:
            break


main()