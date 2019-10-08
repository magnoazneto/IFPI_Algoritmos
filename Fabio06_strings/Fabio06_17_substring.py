from string_tools import substring as substr
def main():
    string = input('Digite uma string qualquer: ')
    begin = int(input('Ponto de partida: '))
    end = int(input('Quantos caracteres? '))
    sub_str = substr(string, begin, begin+end+1)
    print('Substring: ', sub_str)
    

main()
