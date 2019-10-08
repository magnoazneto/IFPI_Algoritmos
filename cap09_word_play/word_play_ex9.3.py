from string_list_tools import strip_str
def main():
    fin = open('words.txt')
    chars = input('Digite as letras proibidas:\n>> ')
    total_words = 0
    words = 0
    for line in fin:
        if avoids(line, chars):
            print_line(line)
            words += 1
        total_words += 1
    print('Total de palavras:', total_words)
    print('Palavras impressas:', words)
    print('Porcentagem: {:.2f} %'.format((percent(total_words, words))))


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()


def avoids(word, cant_chars):
    for l in range(0, len(word)):
        for i in range(0, len(cant_chars)):
            if cant_chars[i] == word[l]:
                return False
    return True


def percent(total, qtd):
    return (100*qtd)/total


if __name__ == '__main__':
    main()