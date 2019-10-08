def main():
    string = input('Digite um nome de variável: ')
    id_type = identify_type(string) 
    if id_type == 'CamelCase':
        print('Pep8:', change_format(string))

    elif id_type == 'Pep8':
        print('CamelCase:', change_format(string))

    else:
        print(id_type)


def change_format(string):
    try:
        i = 0
        new_str = ''
        while i < len(string):
            if ord(string[i]) >= 65 and ord(string[i]) <= 90:
                new_str += '_' + chr(ord(string[i]) + 32)
            elif string[i] == '_':
                if is_letter(string[i+1]):
                    if ord(string[i+1]) >= 65 and ord(string[i+1]) <= 90:
                        return 'nome de variável com formatação mista.'
                    new_str += chr(ord(string[i+1]) - 32)
                    i += 1
            else:
                new_str += string[i]
            i += 1
        return new_str
    except IndexError:
        return 'nomeações em Pep8 não podem terminar em "_"'
            

def identify_type(string):
    if len(string) < 1: return 'Não há string a ser convertida.'
    if ord(string[0]) >= 65 and ord(string[0]) <= 90:
        return 'Não há traços de CamelCase nem Pep8'
    i = 0
    while i < len(string):
        if ord(string[i]) >= 65 and ord(string[i]) <= 90:
            return 'CamelCase'
        elif string[i] == '_':
            return 'Pep8'
        i += 1
    return 'Não há traços de CamelCase nem Pep8'


def is_letter(char):
    codigo = ord(char)
    return codigo >= 65 and codigo <= 90 or codigo >= 97 and codigo <= 122
        

main()
