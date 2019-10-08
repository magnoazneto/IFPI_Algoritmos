from arquivo_utils import abrir_arquivo
from utils import *


def main():
    data_base = import_data('enem2014_nota_por_escola.txt.csv', 'ISO-8859-1')
    #show_data_base(data_base[::-1])
    for line in data_base:
        if 'TERESINA' in line['nome']:
            print_line(line)


def print_line(line):
    print('\nRanking: ' + str(line['ranking']) + '\n' \
            + 'Nome: ' + line['nome'] + '\n' \
            + 'Municipio: ' + line['municipio'] + '\tUF: ' + line['uf'] + '\n' \
            + 'Rede: ' + line['rede'] + '\n' + 'Permanência: ' + line['permanencia'] + '\n' \
            + 'Nv. Socio-Econômico: ' + line['nivel_socio_economico'] + '\n' \
            + 'Objetivas: ' + str(line['media_objetivas']) + '\n' \
            + 'Linguagens: ' + str(line['linguagens']) + '\n' \
            + 'Matematica: ' + str(line['matematica']) + '\n' \
            + 'Natureza: ' + str(line['ciencias_natureza']) + '\n' \
            + 'Humanas: ' + str(line['humanas']) + '\n' \
            + 'Redacao: ' + str(line['redacao']) + '\n' + '***' * 15)


def show_data_base(data_base):
    for line in data_base:
        print_line(line)
        

def import_data(file_name, encoding_type):
    fin = open(file_name, encoding = encoding_type)
    data_extract = fin.readlines()
    output = []
    for line in data_extract:
        line = line.strip().split(';')
        element = {'ranking': int(line[0]), 'nome': line[1],
            'municipio': line[2], 'uf': line[3], 'rede': line[4],
            'permanencia': line[5], 'nivel_socio_economico': line[6],
            'media_objetivas': float('.'.join(line[7].split(','))),
            'linguagens': float('.'.join(line[8].split(','))),
            'matematica': float('.'.join(line[9].split(','))),
            'ciencias_natureza': float('.'.join(line[10].split(','))),
            'humanas': float('.'.join(line[11].split(','))),
            'redacao': float('.'.join(line[12].split(','))), }
        output.append(element)

    return output


main()
