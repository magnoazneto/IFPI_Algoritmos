import getpass
def main():
    senha = 'abcde123'
    string = getpass.getpass('Digite sua senha: ')
    while senha != string:
        print('Senha incorreta!')
        print('Digitada: ', end= '')
        print('*' * (len(string)))
        string = getpass.getpass('Digite sua senha: ')
    print('Senha correta! Acesso concedido.')


main()
