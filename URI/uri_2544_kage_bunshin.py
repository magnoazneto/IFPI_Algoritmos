def main():
    while True:
        try:
            bunshins = int(input())
            jutsus = 0
            while (bunshins > 1):
                bunshins = bunshins / 2
                jutsus += 1
            
            print(jutsus)

        except EOFError:
            break


main()
