from string_tools import get_string_max
def main():
    text = get_string_max(20, 'Digite um texto de 20 caracteres: ')
    diagonal(text)


def diagonal(text):
    i = 0
    spaces = ''
    while i < len(text):
        print(spaces + text[i])
        spaces += ' '
        i += 1
    


main()
