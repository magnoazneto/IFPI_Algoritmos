from string_tools import *
def main():
    string = input('Primeiro, digite uma string qualquer: ')
    target = input('Digite o que deverá ser retirado: ')
    piece = input('Digite o que deverá ser inserido no lugar: ')
    final_string = replace_all(string, target, piece)
    print(final_string)


def replace_all(string, target, piece):  # substitui todas as ocorrencias do target por piece
    i = 0
    new_str = ''
    limit = len(string) - len(target)
    while i < len(string):
        if i <= limit and substring(string, i, i+len(target)) == target:
            new_str += piece
            i += len(target) - 1
        else:
            new_str += string[i]
        i += 1
    return new_str



main()
