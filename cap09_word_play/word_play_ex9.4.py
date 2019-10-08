from string_list_tools import its_in
def main():
    fin = open('words.txt')
    allowed = input('As palavras podem ter quais letras?\n>> ')
    for lines in fin:
        if uses_only(lines, allowed):
            print_line(lines)


def uses_only(word, allowed):
    for i in range(0, len(word)-1):
        if not its_in(allowed, word[i]):
            return False
    return True


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()

if __name__ == '__main__':
    main()