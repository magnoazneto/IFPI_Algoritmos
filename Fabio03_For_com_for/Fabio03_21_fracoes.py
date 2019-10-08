def main():
    numerador = 1
    somatorio = 0
    for denominador in range(1, 51):
        somatorio += (numerador/denominador)
        #print(f'{numerador}/{denominador}')
        numerador += 2
    print(f'Somatório: {somatorio:.2f}')
    

main()
