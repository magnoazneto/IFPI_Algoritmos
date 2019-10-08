from string_tools import number_check
def main():
    string = input()
    count = 0
    while count < len(string):
        if number_check(string[count]):
            print(number_filter(string[count]), end='')
        else:
            print(string[count], end='')
        count += 1
    print()


def number_filter(number):
    if number == '0':
        return 'zero'
    elif number == '1':
        return 'um'
    elif number == '2':
        return 'dois'
    elif number == '3':
        return 'três'
    elif number == '4':
        return 'quatro'
    elif number == '5':
        return 'cinco'
    elif number == '6':
        return 'seis'
    elif number == '7':
        return 'sete'
    elif number == '8':
        return 'oito'
    else:
        return 'nove'
        


main()
