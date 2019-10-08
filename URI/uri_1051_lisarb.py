def main():
    salario = float(input())
    if calcula_IR(salario) != 'Isento':
        print('R$ {:.2f}'.format(calcula_IR(salario)))
    else:
        print(calcula_IR(salario))


def calcula_IR(salario):
    if salario <= 2000:
        return 'Isento'
    elif salario <= 3000:
        salario_trib = salario - 2000
        imposto_8 = salario_trib * 0.08
        return imposto_8
    elif salario <= 4500:
        salario_trib = salario - 2000
        imposto_18 = (salario - 3000) * 0.18
        imposto_8 = 80
        return (imposto_18+imposto_8)
    else:
        salario_trib = salario - 2000
        imposto_8 = 80
        imposto_18 = 270
        imposto_28 = (salario - 4500) * 0.28
        return (imposto_8+imposto_18+imposto_28)


main()
    