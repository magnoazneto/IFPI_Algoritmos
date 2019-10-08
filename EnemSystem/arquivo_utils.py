def novo_arquivo(nome):
    arquivo = open(nome, 'w+')
    print('Arquivo com o nome "%s" criado.' % nome)
    arquivo.close()
    return arquivo


def abrir_arquivo(nome):
    try:
        arquivo = open(nome)
        return arquivo
    except FileNotFoundError:
        print('Base de dados inexistente.')


def abrir_ou_criar(nome):
    try:
        arquivo = open(nome)
        return arquivo
    except FileNotFoundError:
        arquivo = open(nome, 'w+')
        return arquivo    


def gravar_em_arquivo(linhas, nome):
    arquivo = open(nome, 'w')
    for i in range(len(linhas)):
        arquivo.write(linhas[i])
    
    arquivo.close()


def acrescentar_em_arquivo(linhas, nome):
    arquivo = open(nome, 'a')
    for i in range(len(linhas)):
        arquivo.write(linhas[i])
    
    arquivo.close()


if __name__ == '__main__':
    main()