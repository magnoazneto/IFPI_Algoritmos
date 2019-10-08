from utilidades import get_number
def main():
    habitantes = int(get_number('Nº de habitantes a ser analisado: '))
    contador = salario = 1
    media_sal = media_filhos = ate_mil = 0
    somatorio_sal = somatorio_filhos = 0
    while contador <= habitantes:
        print(f'{contador}º habitante: ')
        salario += get_number('Salario: ')
        if salario <= 1000:
            ate_mil += 1
        media_sal += salario
        media_filhos += int(get_number('Filhos: '))
        contador += 1
    media_sal = media_sal / habitantes
    media_filhos = media_filhos / habitantes
    percentual = (100*ate_mil) / habitantes
    print(f'Média salarial: R$ {media_sal:.2f}')
    print(f'Média de filhos: {media_filhos:.2f}')
    print(f'Percentual com salário abaixo de 1000: {percentual:.1f}%')


main()