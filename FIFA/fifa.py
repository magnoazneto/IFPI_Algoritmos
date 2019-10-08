from os import system
from arquivo_utils import *
from utils import *

CSV_FILE_NAME = 'Partidas_CopaMundo_1930_2014.csv'

def main():
    arquivo = open(CSV_FILE_NAME, encoding='ISO-8859-1')
    matches_db = arquivo.readlines()
    arquivo.close()
    LEGENDA = matches_db[0].strip().split(';')
    matrix_base = format_db_to_matrix(LEGENDA, matches_db[1:], ';')
    while True:
        menu()
        option = get_option('\n>> ', 0, 9)
        if option == 1:
            show_matrix(matrix_base)
            wait()
        elif option == 2:
            filter_gols_per_country(matrix_base)
            wait()
        elif option == 3:
            show_matches_per_country(matrix_base)
            wait()
        elif option == 4:
            show_matches_by_stage(matrix_base, 'Final')
            wait()
        elif option == 5:
            show_matches_by_placar(matrix_base)
            wait()
        elif option == 6:
            show_medias(matrix_base)
            wait()
        elif option == 7:
            show_total_gols(matrix_base)
            wait()
        elif optino == 8:
            top_games_per_filter(matrix_base)
            wait()
        elif option == 0:
            print('Saindo!')
            break


def menu():
    cabecalho('FIFA 1930 - 2014')
    print('1 - MOSTRAR TODOS OS JOGOS' \
        + '\n2 - FILTRAR GOLS POR SELEÇÃO' \
        + '\n3 - LISTAR JOGOS POR SELEÇÃO' \
        + '\n4 - LISTAR FINAIS DE COPA DO MUNDO' \
        + '\n5 - LISTAR JOGOS POR PLACAR' \
        + '\n6 - MEDIA DE GOLS' \
        + '\n7 - TOTAL DE GOLS' \
        + '\n8 - TOP JOGOS POR FILTRO' \
        +'\n\n0 - SAIR')


def show_matrix(matrix_base):
    cabecalho('LISTAGEM DE TODOS OS JOGOS')
    for line in matrix_base:
        print(f"\nDATA E HORA: {line['DATAHORA']}" \
            + f"\nFASE: {line['FASE']} \t ESTADIO: {line['ESTADIO']}" \
            + f"\t CIDADE: {line['CIDADE']}" \
            + f"\n===== {line['TIME_CASA']} {line['TIME_CASA_GOLS']}" \
            + f" x {line['TIME_FORA_GOLS']} {line['TIME_FORA']} =====" \
            + f"\nTOTAL DE GOLS: {line['TOTAL_GOLS']}\tRESULTADO: {line['RESULTADO']}")

    print('\nTOTAL:', len(matrix_base))


def filter_gols_per_country(matrix_base):
    # reduce function
    cabecalho('FILTRAGEM DE GOLS POR PAÍS')
    county = input('DIGITE O NOME DE UM PAÍS: ').strip().upper()
    gols = 0
    found = False
    for line in matrix_base:
        if line['TIME_CASA'].upper() == county:
            gols += line['TIME_CASA_GOLS']
            found = True
        elif line['TIME_FORA'].upper() == county:
            gols += line['TIME_FORA_GOLS']
            found = True
    
    print(f'O país {county} já fez {gols} gols de 1930 até 2014!' if found else 'País não encontrado.')


def show_matches_per_country(matrix_base):
    cabecalho('FILTRAR JOGOS POR SELEÇAO')
    games = []
    country = input('DIGITE O NOME DE UM PAÍS: ').strip().upper()
    for line in matrix_base:
        if line['TIME_FORA'].upper() == country or line['TIME_CASA'].upper() == country:
            games.append(line)
    
    games_ordened = games[::-1]
    show_matrix(games_ordened)


def show_matches_by_stage(matrix_base, stage):
    cabecalho(f'MOSTRANDO JOGOS DE FASE "{stage.upper()}"')
    games = []
    for line in matrix_base:
        if line['FASE'] == stage:
            games.append(line)
    
    games_ordened = games[::-1]
    show_matrix(games_ordened)


def show_matches_by_placar(matrix_base):
    cabecalho('LISTANDO JOGOS POR PLACAR')
    placar = list(map(int, input('DIGITE O PLACAR NO FORMATO A x B:\n').upper().strip().split('X')))
    games = []
    for line in matrix_base:
        if line['TIME_FORA_GOLS'] == placar[0] and line['TIME_CASA_GOLS'] == placar[1] \
            or line['TIME_FORA_GOLS'] == placar[1] and line['TIME_CASA_GOLS'] == placar[0]:
            games.append(line)
    game_ordened = games[::-1]
    show_matrix(game_ordened)


def show_medias(matrix_base):
    cabecalho('MENU DE MEDIAS')
    option = get_option('1 - MEDIA DE GOLS EM FINAIS\n2 - MEDIA DE GOLS POR ANO\n3 - MEDIA GERAL DE GOLS\n>> ', 1, 4)
    if option == 1:
        show_result_by_attibute(matrix_base, 'FASE', 'Final')
    elif option == 2:
        year = get_inteiro('\nDE QUE ANO? ')
        show_result_by_attibute(matrix_base, 'ANO', year)
    elif option == 3:
        show_result_by_attibute(matrix_base)
    

def show_result_by_attibute(matrix_base, atribute = None, atribute_value = None, total = False):
    media = 0
    counter = 0
    for line in matrix_base:
        if atribute:
            if line[atribute] == atribute_value:
                if not total: media += line['TOTAL_GOLS']
                counter += 1
        else:
            if not total: media += line['TOTAL_GOLS']
            counter += 1

    if not total:
        media = media / counter
        print(f'Média de Gols: {media:.2f}')
    else:
        print(f'Total de Gols: {counter}')


def show_total_gols(matrix_base):
    cabecalho('FILTRAR O TOTAL DE GOLS')
    option = get_option('1 - TOTAL POR ANO\n2 - TOTAL POR SELEÇÃO\n>> ', 1, 3)
    if option == 1:
        year = get_inteiro('DE QUE ANO? ')
        show_result_by_attibute(matrix_base, 'ANO', year, True)
    elif option == 2:
        show_all_by_country(matrix_base)


def show_all_by_country(matrix_base):
    country = input('PAÍS: ').upper()
    feitos = 0
    pegos = 0
    for line in matrix_base:
        if line['TIME_CASA'].upper() == country:
            feitos += line['TIME_CASA_GOLS']
            pegos += line['TIME_FORA_GOLS']
        elif line['TIME_FORA'].upper() == country:
            feitos += line['TIME_FORA_GOLS']
            pegos += line['TIME_CASA_GOLS']
    
    print(f'O PAIS "{country}" JA FEZ {feitos} GOLS E TOMOU {pegos} GOLS.')


def top_games_per_filter(matrix_base):
    cabecalho('TOP JOGOS POR FILTRO')
    option = get_option('1 - POR QUANTIDADE DE GOLS DO VENCEDOR\n2 - POR TOTAL DE GOLS\n>> ', 1, 3)
    qtd = get_inteiro('LISTAR QUANTOS JOGOS? ')
    seek_top_n(matrix_base, option, qtd)


def seek_top_n(matrix_base, option, size):
    bigger = 0
    counter = 0
    if option == 1:
        for line in matrix_base:
            winner =
    else:

        



def format_db_to_matrix(identifier, data_base, splitter):
    new_matrix = []
    for item in range(len(data_base)):
        line = data_base[item].strip().split(splitter)
        item = {}
        for i in range(len(line)):
            if line[i].isnumeric():
                item[identifier[i]] = int(line[i])
            else:
                item[identifier[i]] = line[i]
        item['TOTAL_GOLS'] = item['TIME_CASA_GOLS'] + item['TIME_FORA_GOLS']
        if item['TIME_CASA_GOLS'] == item['TIME_FORA_GOLS']:
            item['RESULTADO'] = 'EMPATE'
        elif item['TIME_CASA_GOLS'] > item['TIME_FORA_GOLS']:
            item['RESULTADO'] = item['TIME_CASA']
        else:
            item['RESULTADO'] = item['TIME_FORA']
        new_matrix.append(item)

    return new_matrix

        
        

main()