def main():
    entrega, data_final = map(int, input().split())
    print(tcc(entrega, data_final))


def tcc(entrega, data_final):
    new_str = ''
    if entrega > data_final or data_final > 25:
        new_str += 'Eu odeio a profesora!'
        return new_str
    elif data_final - entrega >= 3:
        new_str += 'Muito bem! Apresenta antes do Natal!"'
        return new_str
    else:
        new_str += "Parece o trabalho do meu filho!\n" 
        if data_final + 2 > 24:
            new_str += "Fail! Entao eh nataaaaal!"
            return new_str
        else:
            new_str += "TCC Apresentado!"
            return new_str


main()
