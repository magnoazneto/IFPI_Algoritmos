def main():
    denominador = numerador = 1
    somatorio = 0
    while denominador <= 50:
        somatorio += (numerador/denominador)
        #print(f'{numerador}/{denominador}')
        denominador += 1
        numerador += 2
    print(f'Somatório: {somatorio:.2f}')
    

main()
