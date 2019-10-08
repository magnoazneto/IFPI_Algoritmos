from string_tools import get_string, substring
def main():
    data = get_string(10, 'Digite a data no formato DD/MM/AAAA: ')
    count = 0
    print_data(data)


def print_data(data):
    dia = substring(data, 0, 2)
    mes = substring(data, 3, 5)
    ano = substring(data, 6, 10)
    dia = filtro_dia(int(dia))
    mes = filtro_mes(int(mes))
    if mes and dia:
        print(dia, 'de', mes, 'de', ano)
    else:
        print('Data inválida.')


def filtro_dia(dia):
    return dia if dia < 32 and dia > 0 else False


def filtro_mes(mes):
    if mes == 1:
        return 'Janeiro'
    elif mes == 2:
        return 'Fevereiro'
    elif mes == 3:
        return 'Março'
    elif mes == 4:
        return 'Abril'
    elif mes == 5:
        return 'Maio'
    elif mes == 6:
        return 'Junho'
    elif mes == 7:
        return 'Julho'
    elif mes == 8:
        return 'Agosto'
    elif mes == 9:
        return 'Setembro'
    elif mes == 10:
        return 'Outubro'
    elif mes == 11:
        return 'Novembro'
    elif mes == 12:
        return 'Dezembro'
    else:
        return False


main()
