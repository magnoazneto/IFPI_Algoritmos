from os import system
def cabecalho(msg):
    system('clear')
    print('\n============= '+ msg +' =============')
    print('*' * 27 + '*' * len(msg))

def get_option(msg, begin, end):
    opc = int(input(msg))
    while opc not in range(begin, end):
        print('OPCAO INVALIDA!')
        opc = int(input(msg))
    return opc


def make_array(lenght, value=0):
    return [value] * lenght


def transfer(array1, array2):
    for i in range(len(array1)):
        array2[i] = array1[i]


def add_at_last(array, element):
    new_array = make_array(len(array)+1)
    transfer(array, new_array)
    new_array[len(new_array)-1] = element
    return new_array


def get_inteiro(mensagem):  # INT, sem restrição.
    try:
        return int(input(mensagem))
    except ValueError:
        print('Valor inválido.')
        return get_inteiro(mensagem)


def get_number(mensagem):  # FLOAT, sem restrição.
    try:
        return float(input(mensagem))
    except:
        print('Valor inválido.')
        return get_number(mensagem)


def wait():
    input('Pressione qualquer tecla para continuar')
    system('clear')


def fill_with(string, lenght):
    if len(string) < lenght:
        return string + (' '*(lenght - (len(string))))
    else:
        return string


def filtro_por_prioridade(matriz, prioridade):
    melhor = make_array(len(matriz[0]))
    for i in range(len(matriz)):
        if float(matriz[i][prioridade]) > float(melhor[prioridade]):
            melhor = matriz[i]
    
    return melhor


def show_data_base(data_base, msg, format_func, printer_func):
    print(msg)
    for i in range(len(data_base)):
        celular = format_func(data_base[i])
        print('%d:' %(i+1), end = ' ')
        printer_func(celular)


def formatar_para_arquivo(vetor, separador):
    tamanho = len(vetor)
    formatado = ''
    for i in range(tamanho):
        if i != (tamanho-1):
            formatado += str(vetor[i]) + separador
        else:
            formatado += str(vetor[i])

    return formatado


if __name__ == "__main__":
    main()