def main():
    dia = int(input('Digite o número da semana (de 1 a 7): '))
    dia_selecionado = filtra_dia(dia)
    print(dia_selecionado)


def filtra_dia(dia):
    if dia == 1:
        dia_selecionado = 'Domingo'
    elif dia == 2:
        dia_selecionado = 'Segunda'
    elif dia == 3:
        dia_selecionado = 'Terça'
    elif dia == 4
        dia_selecionado = 'Quarta'
    elif dia == 5:
        dia_selecionado = 'Quinta'
    elif dia == 6:
        dia_selecionado = 'Sexta'
    elif dia == 7:
        dia_selecionado = 'Sábado'
    else:
        dia_selecionado = 'Valor inválido'
    return dia_selecionado


if __name__ == '__main__':
    main()