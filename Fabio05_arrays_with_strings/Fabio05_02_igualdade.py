def main():
    strA = input()
    print('Existem elementos iguais!' if equality_char(strA)\
    else 'Não existem iguais!')    


def equality_char(string):
    count = 0
    count2 = 0
    string_aux = string
    equality = 0
    while count < len(string):
        while count2 < len(string):
            if string[count] == string_aux[count2]:
                equality += 1
                if equality == 2: return True
            count2 += 1
        count += 1
        count2 = 0
        equality = 0
    return False


main()