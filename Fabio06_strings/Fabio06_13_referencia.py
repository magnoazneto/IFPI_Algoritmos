from string_tools import reverse_string, substring
def main():
    name = input()
   # abnt_print_pythonic(name)
    abnt_print_romantic(name)


def abnt_print_pythonic(name):
    ''' Essa seria uma solução mais enxuta, 
    usando o resultado do Split() que na verdade 
    é uma lista.'''
    name = name.split()
    last_name = name[-1]
    i = 0
    letters = ''
    while i < len(name) - 1:
        codigo = ord(name[i][0]) 
        if codigo >= 65 and codigo < 90:
            letters += name[i][0] + '. '
        i += 1
    print(last_name + ', ' + letters)


def abnt_print_romantic(name):
    # Essa seria uma possível solução mais 'romântica'
    last_name = get_last_name(name)
    rest_name = substring(name, 0, len(name) - len(last_name))
    letters = ''
    i = 0
    while i < len(rest_name):
        codigo = ord(rest_name[i])
        if codigo >= 65 and codigo <= 90:
            letters += rest_name[i] + '. '
        i += 1
    print(last_name + ', ' + letters)


def get_last_name(name):
    reversed_string = reverse_string(name)
    last_name = ''
    i = 0
    while i < len(reversed_string):
        if reversed_string[i] == ' ':
            break
        else:
            last_name += reversed_string[i]
        i += 1
    return reverse_string(last_name)

    
            



main()
