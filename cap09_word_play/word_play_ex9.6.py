def main():
    fin = open('words.txt')
    words = 0
    for line in fin:
        if is_abcedarian(line):
            print_line(line)
            words += 1
    print(f'Palavras em ordem alfabética: {words}')


def is_abcedarian(word):
    codigo = ord(word[0])
    for i in range(1, len(word)-1):
        if ord(word[i]) < codigo:
            return False
        codigo = ord(word[i])
    return True


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()


if __name__ == "__main__":
    main()
