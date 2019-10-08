from string_list_tools import its_in
def main():
    fin = open('words.txt')
    wanted = input('As palavras devem ter quais letras?\n>> ')
    for lines in fin:
        if uses_all(lines, wanted):
            print_line(lines)


def uses_all(word, wanted):
    for i in range(0, len(wanted)):
        if not its_in(word, wanted[i]):
            return False
    return True


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()

if __name__ == '__main__':
    main()