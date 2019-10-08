def main():
    while True:
        try:
            password = input()
            print('Senha valida.' if verify(password) else 'Senha invalida.')

        except EOFError:
            break


def verify(password):
    if len(password) < 6 or len(password) > 32: return False
    if ' ' in password: return False
    if not(is_alphanumeric(password)): return False
    count = 0
    uppercase = 0
    lowercase = 0
    numbers = 0
    while count < len(password):
        if ord(password[count]) >= 65 and ord(password[count]) <= 90:
            uppercase += 1
        elif ord(password[count]) >= 97 and ord(password[count]) <= 122:
            lowercase += 1
        elif is_number(password[count]):
            numbers += 1
        count += 1
    if uppercase < 1 or lowercase < 1 or numbers < 1: return False
    return True


def is_alphanumeric(string): # checa se todos os caracteres de uma string são letras ou números
    count = 0
    while count < len(string):
        if not(is_letter(string[count]) or is_number(string[count])):
            return False
        count += 1
    return True


def is_letter(char):  # checa se o caractere é uma letra
    codigo = ord(char)
    if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
        return True
    else:
        return False


def is_number(char):  # checa se uma string é formada apenas por números
    if ord(char) < 48 or ord(char) > 57:
        return False
    else:
        return True


main()
