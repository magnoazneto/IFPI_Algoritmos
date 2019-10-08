import os
from time import sleep as loading

def main():
    while True:
        os.system('clear')
        menu('BOLSA FAMILIA')
        opc = get_option('>> ', 1, 8)
        familias = open('familias.txt')
        if opc == 1:
            show_database(familias)
        elif opc == 2:
            insert_family()
            print('Operação realizada com sucesso!')
        elif opc == 3:
            delete_family(familias)
            print('Operação realizada com sucesso!')
        elif opc == 4:
            edit_family(familias)
            print('Operação realizada com sucesso!')
        elif opc == 5:
            search(familias)
        elif opc == 6:
            search_qtd(familias)
        elif opc == 7:
            print('Adios, amigo!')
            break
        input('Pressione qualquer tecla para continuar')
        for i in range(101):
            print(f'Loading {i} %', flush = True)
            print(('=' * i) + '=>')
            loading(0.01)
            os.system('clear')
            

def insert_family():
    os.system('clear')
    cabecalho('INSERIR NOVA FAMILIA')
    nome_familia = input('NOME DA FAMILIA: ')
    renda = float(input('RENDA DA FAMILIA: '))
    new_family = nome_familia + '-' + str(renda) + '-'
    members = int(input('QUANTIDADE DE MEMBROS: '))
    for i in range(members):
        member = make_array(3)
        print('>>> MEMBRO %d: ' % (i+1))
        member[0] = input('NOME: ')
        new_family += member[0] + '#'
        member[1] = input('SEXO: ')
        new_family += member[1] + '#'
        member[2] = get_inteiro('IDADE: ')
        new_family += str(member[2])
        # members = add_at_last(members, member)
        if i < members - 1:
            new_family += '*'
    arquivo = open('familias.txt', 'a')
    arquivo.write(new_family + '\n')
    arquivo.close()


def search(familias):
    os.system('clear')
    cabecalho('BUSCA POR ATRIBUTO')
    print('\n1 - FAIXA DE RENDA')
    print('\n2 - QUANTIDADE DE MEMBROS')
    print('\n3 - RENDA PER CAPITA')
    option = get_option('\n>> ', 1, 4)
    if option == 1:
        search_by_cash(familias)
    elif option == 2:
        search_by_members(familias)
    elif option == 3:
        search_by_rent_per_member(familias)


def search_by_cash(familias):
    data_base = familias.readlines()
    cash_min = get_number('DIGITE O LIMITE INFERIOR: ')
    cash_max = get_number('DIGITE O LIMITE SUPERIOR: ')
    #print(data_base)
    cabecalho('RESULTADOS DA BUSCA')
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        if float(family[1]) >= cash_min and float(family[1]) <= cash_max:
            show_family(family)


def search_by_members(familias):
    data_base = familias.readlines()
    qtd_min = get_inteiro('QUANTIDADE MÍNIMA: ')
    qtd_max = get_inteiro('QUANTIDADE MÁXIMA: ')
    cabecalho('RESULTADOS DA BUSCA')
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        members = family[2].strip().split('*')
        if len(members) >= qtd_min and len(members) <= qtd_max:
            show_family(family)


def search_by_rent_per_member(familias):
    data_base = familias.readlines()
    cash_min = get_number('DIGITE O LIMITE INFERIOR: ')
    cash_max = get_number('DIGITE O LIMITE SUPERIOR: ')
    cabecalho('RESULTADOS DA BUSCA')
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        members = family[2].strip().split('*')
        cash_per_member = float(family[1]) / len(members)
        if cash_per_member >= cash_min and cash_per_member <= cash_max:
            show_family(family)
    

def search_qtd(familias):
    os.system('clear')
    cabecalho('BUSCA POR QUANTIDADE')
    print('SELECIONE UM FILTRO\n' \
        + '\n1 - MEMBROS' \
        + '\n2 - RENDA MÁXIMA' \
        + '\n3 - SEXO')
    option = get_option('\n>> ', 1, 4)
    if option == 1:
        filter_by_qtd_members(familias)
    elif option == 2:
        filter_by_cash(familias)
    elif option == 3:
        filter_by_sex(familias)


def filter_by_sex(familias):
    os.system('clear')
    print('DIGITE M PARA MASCULINO, E F PARA FEMININO:')
    option = input('\n>> ')
    while option != 'M' and option != 'F':
        print('M para Masculino! F para Feminino!')
        option = input('>> ')
    data_base = familias.readlines()
    quantidade = 0
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        members = family[2].strip().split('*')
        for m in range(len(members)):
            member = members[m].split('#')
            if member[1] == option: quantidade += 1
    
    print('==================================')
    print('%d pessoa(s) encontrada(s).' % quantidade)


def filter_by_cash(familias):
    os.system('clear')
    cash = get_number('DIGITE A RENDA MÁXIMA: ')
    data_base = familias.readlines()
    quantidade = 0
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        if float(family[1]) <= cash: quantidade += 1
    
    print('==================================')
    print('%d familia(s) encontrada(s).' % quantidade)


def filter_by_qtd_members(familias):
    os.system('clear')
    qtd_max = get_inteiro('QUANTIDADE DE MEMBROS MÁXIMA DA FAMILIA: ')
    data_base = familias.readlines()
    quantidade = 0
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        members = family[2].strip().split('*')
        if len(members) <= qtd_max: quantidade += 1
    
    print('==================================')
    print('%d familia(s) encontrada(s).' % quantidade)


def edit_family(familias):
    os.system('clear')
    data_base = familias.readlines()
    list_all_by_name(data_base)
    print('\nFAMILIA A EDITAR: ')
    option = get_option('\n>> ', 1, len(data_base) + 1)
    family = get_family(data_base[option-1])
    os.system('clear')
    show_family(family)
    #print(family)
    print('\nDADO A EDITAR:')
    menu = '1 - NOME' \
        +  '\n2 - RENDA' \
        +  '\n3 - MEMBROS'
    print(menu)
    dado = get_option('\n>> ', 1, 5)
    new_db = ''
    if dado == 1:
        novo_nome = input('Novo nome:\n>> ')
    elif dado == 2:
        nova_renda = get_number('Nova renda:\n>> ')
    for i in range(len(data_base)):
        if (i+1) != option:
            new_db += data_base[i]
        else:
            if dado == 1:
                family[0] = novo_nome
            elif dado == 2:
                family[1] = str(nova_renda)
            elif dado == 3:
                family[2] = edit_members(family)
            new_family = family[0] + '-' + family[1] + '-' + family[2]
            new_db += new_family + '\n'

    arquivo = open('familias.txt', 'w')
    arquivo.write(new_db)
    arquivo.close()


def edit_members(family):
    os.system('clear')
    members = family[2].split('*')
    for m in range(len(members)):
        member = members[m].split('#')
        print('>>> MEMBRO %d:' % (m+1))
        print('\tNOME:', member[0])
        print('\tSEXO:', member[1])
        print('\tIDADE:', member[2])
    option = get_option('\nMEMBRO A EDITAR:\n\n(PARA INSERIR UM NOVO, DIGITE 0)\n>> ', 0, len(members)+1)
    if option == 0:
        print('NOVO MEMBRO: ')
        member = make_array(3)
        new_member = ''
        member[0] = input('>>NOME: ')
        new_member += member[0] + '#'
        member[1] = input('>>SEXO: ')
        new_member += member[1] + '#'
        member[2] = get_inteiro('>>IDADE: ')
        new_member += str(member[2])
        members = add_at_last(members, new_member)
        members = '*'.join(members)
        
    else:
        member = members[option-1].split('#')
        print('\n1 - NOME    2 - SEXO   3 - IDADE   0 - [DELETAR MEMBRO]')
        dado = get_option('\nDADO A EDITAR:\n>> ', 0, 4)
        if dado == 0:
            new_members = make_array(0)
            for i in range(len(members)):
                if (i+1) != option:
                    new_members = add_at_last(new_members, members[i])
                
            new_members = '*'.join(new_members)
            return new_members

        elif dado == 1:
            member[0] = input('NOVO NOME:\n>> ')
        elif dado == 2:
            member[1] = input('NOVO SEXO:\n>> ')
        elif dado == 3:
            member[2] = get_inteiro('NOVA IDADE:\n>> ')

        new_member = member[0] + '#' + member[1] + '#' + str(member[2])
        members[option-1] = new_member
        members = '*'.join(members)

    return members
    

def list_all_by_name(data_base):
    print('=====================')
    print('FAMILIAS CADASTRADAS:')
    for i in range(len(data_base)):
        family = get_family(data_base[i])
        print('%d: %s' % ((i+1), family[0]))


def delete_family(familias):
    data_bate = familias.readlines()
    choice = get_option('\nFAMILIA A EXCLUIR:\n>> ', 1, len(data_bate)+1)
    new_db = make_array(0)
    for i in range(len(data_bate)):
        if (i+1) != choice:
            new_db = add_at_last(new_db, data_bate[i])
    arquivo = open('familias.txt', 'w')
    my_base = ''
    for i in range(len(new_db)):
        my_base += new_db[i]
    arquivo.write(my_base)
    arquivo.close()


def show_family(family):
    print('\nFAMILIA:', family[0])
    print('RENDA: %.2f' % float(family[1]))
    members = family[2].split('*')
    print('>>> MEMBROS:')
    print('NOME\t\tSEXO\t\tIDADE')
    for m in range(len(members)):
        member = members[m].split('#')
        print(str(m+1) +': ' + member[0] + '   \t\t' + member[1] + '\t\t' + member[2])


def show_database(familias):
    cabecalho('FAMILIAS CADASTRADAS')
    data_base = familias.readlines()
    for i in range(len(data_base)):
        print('======================')
        print('====== FAMILIA %d =====' % (i+1))
        print('======================')
        family = get_family(data_base[i])
        show_family(family)


def get_family(line):
    family = line.strip().split('-')
    return family


def get_option(msg, begin, end):
    opc = int(input(msg))
    while opc not in range(begin, end):
        print('OPCAO INVALIDA!')
        opc = int(input(msg))
    return opc


def cabecalho(msg):
    print('\n============= '+ msg +' =============')
    print('*' * 27 + '*' * len(msg))


def menu(msg):
    cabecalho(msg)
    options = '1 - MOSTRAR CADASTRO GERAL' \
        + '\n2 - ADICIONAR NOVA FAMILIA' \
        + '\n3 - EXCLUIR FAMILIA' \
        + '\n4 - EDITAR FAMILIA' \
        + '\n5 - REALIZAR BUSCA POR ATRIBUTOS' \
        + '\n6 - REALIZAR BUSCA QUANTITATIVA' \
        + '\n\n7 - SAIR'
    
    print(options)


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

main()
