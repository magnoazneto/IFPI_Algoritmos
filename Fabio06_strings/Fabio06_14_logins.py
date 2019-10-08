def main():
    name = input('Digite seu nome completo: ')
    print(make_login(name))


def make_login(name):
    i = 0
    login = ''
    while i < len(name):
        if is_uppercase(name[i]):
            login += name[i]
        i += 1
    return login


def is_uppercase(char):
    return ord(char) >= 65 and ord(char) <= 90


main()
