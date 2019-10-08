from arquivo_utils import *
from utils import *
from os import system

DATA_BASE_NAME = 'celulares.txt'
LEGENDA = '\nFABRICANTE\tMODELO\t\t\tSO\tM. RAM\tARMAZENAMENTO\tFREQ.\tPROCESSADOR\t\tPRECO MEDIO'

def main():
    while True:
        menu()
        arquivo = abrir_arquivo(DATA_BASE_NAME)
        data_base = arquivo.readlines()
        arquivo.close()
        option = get_option('\nPor favor, escolha uma opção:\n >> ', 0, 8)
        if option == 0:
            print('Tchau!')
            break
        elif option == 1:
            novo_aparelho()
            print('OPERAÇÃO REALIZADA COM SUCESSO!')
        elif option == 2:
            cabecalho('LISTANDO TODOS OS CELULARES')
            lista_celulares(data_base)
        elif option == 3:
            busca_por_atributo(data_base)
        elif option == 4:
            cabecalho('MEDIA DE PRECO DE TODOS OS CELULARES CADASTRADOS')
            resultado = media_por_valor(data_base)
            print('Média: %.2f' % resultado)
        elif option == 5:
            cabecalho('MEDIA DE PRECO DE TODOS DE UMA MARCA')
            resultado = media_por_marca(data_base)
            print('Média: %.2f' % resultado)
        elif option == 6:
            cabecalho('MENOR E MENOR VALOR')
            listar_extremos(data_base)
        elif option == 7:
            cabecalho('ANÁLISE DE CUSTO BENEFÍFICO')
            celular = melhor_custo_beneficio(data_base)
            print('\nMELHOR CUSTO/BENEFÍCIO CONSIDERANDO A PRIORIDADE ESCOLHIDA:')
            print(LEGENDA)    
            show_phone(celular)
        
        wait()


def menu():
    cabecalho('SISTEMA DE CADASTRO DE CELULARES')
    print('1 - NOVO APARELHO' \
        + '\n2 - LISTAR CELULARES' \
        + '\n3 - REALIZAR BUSCA' \
        + '\n4 - CALCULAR MÉDIA DOS VALORES' \
        + '\n5 - CALCULAR MÉDIA POR MARCA' \
        + '\n6 - LISTAR MAIS CARO E MAIS BARATO' \
        + '\n7 - MELHOR CUSTO BENEFICIO' \
        + '\n\n0 - SAIR')

    
def novo_aparelho():
    novo_celular = ''
    abrir_ou_criar(DATA_BASE_NAME)
    cabecalho('INSERIR NOVO APARELHO')
    novo_celular += input('> Fabricante: ').strip().upper() + '#'
    novo_celular += input('> Modelo: ').strip().upper() + '#'
    so = input('> SO: ').strip().upper()
    while so != 'ANDROID' and so != 'IOS':
        print('Sistema Operacional desconhecido. O celular é Android ou IOS?')
        so = input('> SO: ').strip().upper()
    novo_celular += so + '#'
    novo_celular += str(get_number('> Memória RAM (em GigaBytes): ')) + '#'
    novo_celular += str(get_number('> Armazenamento: (em GB): ')) + '#'
    novo_celular += str(get_number('> Frequencia (em Ghz): ')) + '#'
    novo_celular += input('> Processador: ') + '#'
    novo_celular += str(get_number('> Preço médio: ')) + '\n'
    print('\nO APARELHO A SEGUIR SERÁ INSERIDO NO SISTEMA:')
    print(LEGENDA)   
    show_phone(get_phone(novo_celular))
    print('\nCONFIRMA A OPERAÇÃO?')
    option = get_option('\n1 - CONFIRMAR\n2 - REESCREVER\n>> ', 1, 3)
    if option == 1:
        acrescentar_em_arquivo(novo_celular, DATA_BASE_NAME)
    else:
        novo_aparelho()


def lista_celulares(data_base):
    show_data_base(data_base, LEGENDA, get_phone, show_phone)


def busca_por_atributo(data_base):
    cabecalho('FILTRAR CELULARES')
    print('ESCOLHA UMA OPÇÃO:')
    option = get_option('\n1 - FILTRAR POR FABRICANTE\n' \
        + '2 - FILTRAR POR SO\n' \
        + '3 - FILTRAR POR MEMORIA RAM\n' \
        + '4 - FILTRAR POR ARMAZENAMENTO\n' \
        + '5 - FILTRAR POR VALOR\n>> ' , 1, 6)
    if option == 1:
        resultado = filtrar_por_att(data_base, 0, 'FABRICANTE')
        show_data_base(resultado, LEGENDA, get_phone, show_phone)
    elif option == 2:
        resultado = filtrar_por_att(data_base, 2, 'SISTEMA OPERACIONAL')
        show_data_base(resultado, LEGENDA, get_phone, show_phone)
    elif option == 3:
        resultado = filtrar_por_att_numerico(data_base, 3, 'MEMORIA RAM')
        show_data_base(resultado, LEGENDA, get_phone, show_phone)
    elif option == 4:
        resultado = filtrar_por_att_numerico(data_base, 4, 'ARMAZENAMENTO')
        show_data_base(resultado, LEGENDA, get_phone, show_phone)
    elif option == 5:
        resultado = filtrar_por_att_numerico(data_base, 7, 'PRECO MEDIO')
        show_data_base(resultado, LEGENDA, get_phone, show_phone)


def filtrar_por_att(data_base, atributo, msg):
    cabecalho('FILTRO POR ' + msg)
    busca = input('\nDIGITE O %s:\n>> ' % msg).strip().upper()
    resultado = make_array(0)
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if celular[atributo] == busca:
            resultado = add_at_last(resultado, formatar_para_arquivo(celular, '#'))
    
    return resultado


def filtrar_por_att_numerico(data_base, atributo, msg):
    cabecalho('FILTRO POR ' + msg)
    busca = get_number('\n%s MINIMO(A):\n>> ' % msg)
    resultado = make_array(0)
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if float(celular[atributo]) >= busca:
            resultado = add_at_last(resultado, formatar_para_arquivo(celular, '#'))

    return resultado


def media_por_valor(data_base):
    media = 0
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        media = ((media*1000) + (float(celular[7])*1000)) / 1000
    media = media / len(data_base)
    return media


def media_por_marca(data_base):
    marca = input('\nDIGITE UM FABRICANTE:\n>> ').strip().upper()
    media = 0
    quantidade = 0
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if celular[0] == marca:
            media = ((media*1000) + (float(celular[7])*1000)) / 1000
            quantidade += 1
    media = media / quantidade
    return media


def listar_extremos(data_base):
    maior = 0
    menor = 100000000
    mais_caros = make_array(0)
    mais_baratos = make_array(0)
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if float(celular[7]) >= maior:
            if float(celular[7]) == maior:
                mais_caros = add_at_last(mais_caros, formatar_para_arquivo(celular, '#'))
            elif float(celular[7]) > maior:
                maior = float(celular[7])
                mais_caros = make_array(0)
                mais_caros = add_at_last(mais_caros, formatar_para_arquivo(celular, '#'))
        if float(celular[7]) <= menor:
            if float(celular[7]) == menor:
                mais_baratos = add_at_last(mais_baratos, formatar_para_arquivo(celular, '#'))
            elif float(celular[7]) < menor:
                menor = float(celular[7])
                mais_baratos = make_array(0)
                mais_baratos = add_at_last(mais_baratos, formatar_para_arquivo(celular, '#'))
       
    print('\nCELULAR(ES) MAIS CARO(S):')
    show_data_base(mais_caros, LEGENDA, get_phone, show_phone)
    
    print('====='*10)
    print('\nCELULAR(ES) MAIS BARATO(S):')
    show_data_base(mais_baratos, LEGENDA, get_phone, show_phone)


def melhor_custo_beneficio(data_base):
    prioridade = get_option('O QUE É MAIS IMPORTANTE PARA VOCÊ?\n' \
                + '1 - Memória RAM\n' \
                + '2 - Armazenamento\n' \
                + '3 - Processamento\n>> ', 1, 4)
    menor = menor_valor(data_base)
    consideraveis = make_array(0)
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if float(celular[7]) <= (menor + 200):
            consideraveis = add_at_last(consideraveis, celular)
                
    return filtro_por_prioridade(consideraveis, prioridade+2)


def menor_valor(data_base):
    mais_baratos = make_array(0)
    menor = 1000000
    for i in range(len(data_base)):
        celular = get_phone(data_base[i])
        if float(celular[7]) <= menor: 
            if float(celular[7]) == menor:
                mais_baratos = add_at_last(mais_baratos, celular)
            elif float(celular[7]) < menor:
                menor = float(celular[7])
                mais_baratos = make_array(0)
                mais_baratos = add_at_last(mais_baratos, celular)
    
    return float(mais_baratos[0][7])


def get_phone(celular_formatado):
    return celular_formatado.strip().split('#')
    

def show_phone(celular):
    print(fill_with(celular[0], 6)+ '\t'+ fill_with(celular[1], 10) + '\t\t'+ celular[2]+ '\t'+ celular[3]+ '\t' \
        + celular[4]+ '\t\t'+ celular[5]+ '\t'+ fill_with(celular[6], 14) + '\t\t' + celular[7])


main()
