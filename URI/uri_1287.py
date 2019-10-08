def main():
    while True:
        try:
            string = input()
            print(filter_str(string))
        except EOFError:
            break


def filter_str(string):
    i = 0
    new_str = ''
    while i < len(string):
        if is_number(string[i]):
            new_str += string[i]
        elif string[i] == 'l':
            new_str += '1'
        elif string[i] == 'o' or string[i] == 'O':
            new_str += '0'
        elif is_letter(string[i]):
            return 'error'
        i += 1
    if len(new_str) > 0:
        return int(new_str) if int(new_str) <= 2147483647 else 'error'
    else:
        return 'error'
    

def is_letter(char):  # checa se o caractere é uma letra
    codigo = ord(char)
    if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
        return True
    else:
        return False


def is_number(char):  # checa se um char é numero
    return ord(char) >= 48 and ord(char) <= 57
   
main()
