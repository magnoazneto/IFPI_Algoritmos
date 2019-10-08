def main():
    arq = open('amigo.txt')
    base = arq.readlines()
    for i in range(len(base)):
        print(base[i])


main()
