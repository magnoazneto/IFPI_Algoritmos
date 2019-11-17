from os import system
from arquivo_utils import *
from utils import *

DB_VEICULOS_NAME = 'veiculos.txt'
DB_MONTADORAS_NAME = 'montadoras.txt'
LEGENDA_MONTADORAS = '    ID\t\tNOME\t\tPAIS'
LEGENDA_CARROS = '   PLACA\tNOME\t\tMODELO\t\tID_MONTADORA\tKILOMETRAGEM\tPRECO'

def main():
    veiculos = abrir_ou_criar(DB_VEICULOS_NAME)
    montadoras = abrir_ou_criar(DB_MONTADORAS_NAME)
    db_veiculos = veiculos.readlines()
    db_montadoras = montadoras.readlines()
    veiculos.close()
    montadoras.close()
    while True:
        menu()
        option = get_option('\n>> ', 0, 7)
        if option == 1:
            db_veiculos, db_montadoras = cadastrar_veiculo(db_veiculos, db_montadoras)
            wait()
        elif option == 2:
            cabecalho('CARROS CADASTRADOS')
            show_cars(db_veiculos, LEGENDA_CARROS)
            wait()
        elif option == 3:
            cadastrar_montadora(db_montadoras)
        elif option == 4:
            show_montadoras(db_montadoras, LEGENDA_MONTADORAS)
            wait()
        elif option == 5:
            db_veiculos, db_montadoras = edit_databases(db_veiculos, db_montadoras)
            wait()
        elif option == 6:
            db_montadoras, db_veiculos = del_databases(db_montadoras, db_veiculos)
            wait()
        elif option == 0:
            print('Salvando e saindo!')
            gravar_em_arquivo(db_veiculos, DB_VEICULOS_NAME)
            gravar_em_arquivo(db_montadoras, DB_MONTADORAS_NAME)
            break


def cadastrar_veiculo(db_veiculos, db_montadoras):
    cabecalho('CADASTRAR NOVO VEÍCULO')
    if len(db_montadoras) == 0:
        print('NÃO HÁ NENHUMA MONTADORA CADASTRADA AINDA.\nMUDANDO PARA ADIÇÃO DE MONTADORA\n')
        input('pressione qualquer tecla para prosseguir')
        cadastrar_montadora(db_montadoras)
    novo_veiculo = {}
    novo_veiculo['placa'] = get_placa(db_veiculos, 'DIGITE A PLACA NO FORMATO XXX-NNNN: ') 
    novo_veiculo['nome'] = input('DIGITE O NOME DO MODELO:  ')
    novo_veiculo['modelo'] = input('DIGITE O ANO DO MODELO (AAAA/AAAA): ')
    novo_veiculo['id_montadora'] = str(get_montadora(db_montadoras) + 999)
    novo_veiculo['kilometragem'] = float(input('KILOMETRAGEM: '))
    novo_veiculo['preco'] = float(input('DIGITE O PRECO '))
    #acrescentar_em_arquivo(format_car_to_file(novo_veiculo), DB_VEICULOS_NAME)
    db_veiculos += [format_car_to_file(novo_veiculo)]
    print('VEÍCULO ACRESCENTADO!')
    return db_veiculos, db_montadoras


def del_databases(db_montadoras, db_veiculos):
    cabecalho('DELETAR REGISTRO')
    option_del = get_option('1 - DELETAR MONTADORA\n2 - DELETAR VEICULO\n>> ', 1, 3)
    if option_del == 1:
        db_montadoras = del_mont(db_montadoras)
    elif option_del == 2:
        db_veiculos = del_car(db_veiculos)
    
    return db_montadoras, db_veiculos


def del_car(db_veiculos):
    cabecalho('DELETAR REGISTRO DE VEICULO')
    show_cars(db_veiculos, LEGENDA_CARROS)
    option = get_option('SELECIONE O CARRO:\n>> ', 1, len(db_veiculos)+1)
    new_db = []
    for i in range(len(db_veiculos)):
        if i != (option-1):
            new_db += [db_veiculos[i]]
    
    #gravar_em_arquivo(new_db, DB_VEICULOS_NAME)
    print('OPERAÇÃO REALIZADA COM SUCESSO!')
    return new_db


def del_mont(db_montadoras):
    cabecalho('DELETAR REGISTRO DE MONTADORAS')
    show_montadoras(db_montadoras, LEGENDA_MONTADORAS)
    option = get_option('SELECIONE A MONTADORA:\n>> ', 1, len(db_montadoras)+1)
    new_db = []
    for i in range(len(db_montadoras)):
        if i != (option-1):
            new_db += [db_montadoras[i]]
    
    db_montadoras = new_db
    #gravar_em_arquivo(new_db, DB_MONTADORAS_NAME)
    print('OPERAÇÃO REALIZADA COM SUCESSO!')
    return new_db


def get_montadora(db_montadoras):
    show_montadoras(db_montadoras, LEGENDA_MONTADORAS)
    option = get_option('\nESCOLHA UMA MONTADORA, OU DIGITE 0 PARA CADASTRAR UMA NOVA\n>> ', 0, len(db_montadoras)+1)
    while option == 0: 
        cadastrar_montadora(db_montadoras)
        input('pressione qualquer tecla para prosseguir')
        show_montadoras(db_montadoras, LEGENDA_MONTADORAS)
        option = get_option('\nESCOLHA UMA MONTADORA, OU DIGITE 0 PARA CADASTRAR UMA NOVA\n>> ', 0, len(db_montadoras)+1)
    
    return option


def get_placa(db_veiculos, msg):
    placa = input(msg).upper()
    while len(placa) != 8:
        print('A PLACA DEVE CONTER O FORMATO EXATO XXX-NNNN!')
        placa = input(msg).upper()
    for i in range(len(db_veiculos)):
        if format_car_to_dict(db_veiculos[i])['placa'] == placa:
            print('PLACA DUPLICADA. POR FAVOR, VERIFIQUE E INSIRA NOVAMENTE.')
            placa = get_placa(db_veiculos, msg)
    
    return placa
            

def show_cars(db_cars, msg):
    print(msg)
    for i in range(len(db_cars)):
        print('%d: ' % (i+1), end= ' ')
        car = format_car_to_dict(db_cars[i]) 
        print(car['placa'] + '\t' + fill_with(car['nome'], 10) + '\t' + fill_with(car['modelo'], 10) + '\t' \
            + str(car['id_montadora']) + '\t\t' \
            + str(car['kilometragem']) \
            + '\t\t' + str(car['preco']))


def show_montadoras(db_montadoras, msg):
    print(msg)
    for i in range(len(db_montadoras)):
        print('%d: ' % (i+1), end= ' ')
        montadora = format_mont_to_dict(db_montadoras[i]) 
        print(montadora['id'] + '\t' + fill_with(montadora['nome'], 11) + '\t' + montadora['pais'])


def cadastrar_montadora(db_montadoras):
    cabecalho('CADASTRAR NOVA MONTADORA')
    #print(db_montadoras)
    montadora = {}
    montadora['id'] = len(db_montadoras) + 1000
    montadora['nome'] = input('NOME DA MONTADORA: ')
    montadora['pais'] = input('PAIS DA MONTADORA: ')
    db_montadoras += [format_mont_to_file(montadora)]
    #acrescentar_em_arquivo(format_mont_to_file(montadora), DB_MONTADORAS_NAME)

    print('MONTADORA CADASTRADA COM SUCESSO!')


def edit_databases(db_veiculos, db_montadoras):
    cabecalho('EDIÇÃO DE REGISTO')
    option = get_option('1 - EDITAR VEICULO\n' \
        + '2 - EDITAR MONTADORA\n' \
        + '\n>> ', 1, 3)
    if option == 1:
        db_veiculos = edit_car(db_veiculos, db_montadoras)
    else:
        db_montadoras = edit_mont(db_montadoras)
    
    return db_veiculos, db_montadoras

    
def edit_car(db_veiculos, db_montadoras):
    cabecalho('EDIÇÃO DE VEÍCULO')
    show_cars(db_veiculos, LEGENDA_CARROS)
    option_car = get_option('SELECIONE O VEÍCULO:\n>>', 1, len(db_veiculos)+1)
    veiculo = format_car_to_dict(db_veiculos[option_car-1])
    print('O QUE VOCÊ DESEJA ALTERAR?\n' \
        + '1 - PLACA\n' \
        + '2 - NOME\n' \
        + '3 - MODELO\n' \
        + '4 - ID_MONTADORA\n' \
        + '5 - KILOMETRAGEM\n' \
        + '6 - PRECO\n')
    option = get_option('>> ', 1, 7)
    if option == 1:
        veiculo['placa'] = get_placa(db_veiculos, 'DIGITE A PLACA NO FORMATO XXX-NNNN: ')
    elif option == 2:
        veiculo['nome'] = input('DIGITE O NOVO NOME: ')
    elif option == 3:
        veiculo['modelo'] = input('DIGITE O MODELO (AAAA/AAAA): ')
    elif option == 4:
        veiculo['id_montadora'] = str(get_montadora(db_montadoras) + 999)
    elif option == 5:
        veiculo['kilometragem'] = str(get_number('DIGITE A NOVA KILOMETRAGEM: '))
    elif option == 6:
        veiculo['preco'] = str(get_number('NOVO PREÇO: '))

    new_db = []
    for i in range(len(db_veiculos)):
        if i == (option_car-1):
            new_db += [format_car_to_file(veiculo)]
        else:
            new_db += [db_veiculos[i]]
    
    #gravar_em_arquivo(new_db, DB_VEICULOS_NAME)
    print('ALTERACAO EFETUADA COM SUCESSO!')   
    return new_db   


def edit_mont(db_montadoras):
    cabecalho('EDIÇÃO DE MONTADORA')
    show_montadoras(db_montadoras, LEGENDA_MONTADORAS)
    option_mont = get_option('ESCOLHA A MONTADORA\n>> ', 1, len(db_montadoras)+1)
    montadora = format_mont_to_dict(db_montadoras[option_mont-1])
    #print(montadora)
    print('DADO A ALTERAR:')
    option = get_option('\n1 - NOME\n2 - PAIS\n\n>> ', 1, 3)
    if option == 1:
        montadora['nome'] = input('DIGITE O NOVO NOME: ')
    elif option == 2:
        montadora['pais'] = input('DIGITE O NOVO PAIS: ')
    new_db = []
    for i in range(len(db_montadoras)):
        if i == (option_mont-1):
            new_db += [format_mont_to_file(montadora)]
        else:
            new_db += [db_montadoras[i]]

    #gravar_em_arquivo(new_db, DB_MONTADORAS_NAME)
    print('ALTERACAO EFETUADA COM SUCESSO!')
    return new_db

    
def format_mont_to_file(montadora):
    return str(montadora['id']) + '#' + montadora['nome'] + '#' + montadora['pais'] + '\n'


def format_car_to_file(veiculo):
    return veiculo['placa'] + '#' + veiculo['nome'] + '#' + veiculo['modelo'] + '#' + str(veiculo['id_montadora']) \
    + '#' + str(veiculo['kilometragem']) + '#' + str(veiculo['preco']) + '\n'


def format_mont_to_dict(string):
    descompactada = string.strip().split('#')
    concessionaria = {}
    concessionaria['id'] = descompactada[0]
    concessionaria['nome'] = descompactada[1]
    concessionaria['pais'] = descompactada[2]
    return concessionaria


def format_car_to_dict(string):
    descompact = string.split('#')
    veiculo = {}
    veiculo['placa'] = descompact[0]
    veiculo['nome'] = descompact[1]
    veiculo['modelo'] = descompact[2]
    veiculo['id_montadora'] = int(descompact[3])
    veiculo['kilometragem'] = float(descompact[4])
    veiculo['preco'] = float(descompact[5])
    return veiculo


def menu():
    system('clear')
    cabecalho('MENU PRINCIPAL')
    print('1 - ADICIONAR NOVO VEÍCULO\n' \
        + '2 - MOSTRAR VEÍCULOS CADASTRADOS\n' \
        + '3 - CADASTRAR NOVA MONTADORA\n' \
        + '4 - MOSTRAR MONTADORAS CADASTRADAS\n' \
        + '5 - EDITAR REGISTRO\n' \
        + '6 - DELETAR REGISTRO\n' \
        +' \n0 - SAIR')


main()
