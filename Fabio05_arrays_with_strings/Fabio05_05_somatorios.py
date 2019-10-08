def main():
    array = get_string(20, 'Digite um vetor de tamanho 20: ')
    count = 0
    amount = 0
    while count < 10:
        amount += (int(array[count]) - int((array[len(array)-1-count]))) ** 2
        count += 1
    print('Somatório: %i' %(amount))


def get_string(lenght, msg):
    string = input(msg)
    while len(string) != lenght:
        print('Tamanho incorreto, você digitou %i elementos.' % len(string))
        string = input(msg)
    return string


main()
