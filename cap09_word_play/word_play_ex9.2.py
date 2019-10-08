def main():
    fin = open('words.txt')
    words = 0
    total_words = 0
    for line in fin:
        if has_no_e(line):
            print_line(line)
            words += 1
        total_words += 1
    print('Total de palavras:', total_words)
    print('Palavras sem a letra "e":', words)
    print('Porcentagem: {:.2f} %'.format((percent(total_words, words))))


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()


def has_no_e(word):
    for i in range(0, len(word)):
        if word[i] == 'e':
            return False
    return True


def percent(total, qtd):
    return (100*qtd)/total


if __name__ == '__main__':
    main()
