from utilidades import get_int_positivo, get_number
def main():
    fichas = get_int_positivo('Quantas fichas irá cadastrar? ')
    count = 1
    ident = horas_trab = dependentes = salario = inss = ir = 0
    sal_hora = 12.00
    sal_dep = 40.00
    while count <= fichas:
        print(f'{count}º funcionário: ')
        ident = int(get_number(f'ID: '))
        horas_trab = get_number('Horas trabalhadas: ')
        dependentes = int(get_number('Dependentes: '))
        salario = (horas_trab*sal_hora) + (dependentes*sal_dep)
        print(f'Salário bruto: {salario:.2f}')
        inss = salario * 0.085
        print(f'INSS:\t{inss:.2f}')
        ir = salario * 0.05
        print(f'IR:\t{ir:.2f}')
        print(f'Salário Líquido: {salario-ir-inss:.2f}')
        count += 1


main()
