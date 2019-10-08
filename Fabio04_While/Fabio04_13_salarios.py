from utilidades import get_float_positivo
def main():
    salario = get_float_positivo('Salário >> ')
    atuais = reajustados = 0
    while salario != 0:
        reajuste = calcula_reajuste(salario)
        atuais += salario
        novo_salario = salario + (salario*reajuste)
        reajustados += novo_salario
        print(f'Novo salário: R$ {novo_salario:.2f}')
        print(f'Aumento de {reajuste*100} %.')
        salario = get_float_positivo('Salário >> ')
    print(f'Folha de pagamento antiga:\t{atuais:.2f}')
    print(f'Nova folha:\t\t\t{reajustados:.2f}')
    print(f'Diferença no pagamento:\t\t{(reajustados-atuais):.2f}')
    

def calcula_reajuste(salario):
    if salario < 3000:
        return 0.25
    elif salario < 6000:
        return 0.2
    elif salario < 10000:
        return 0.15
    else:
        return 0.10


main()