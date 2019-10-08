def main():
    array = get_number_str('Digite uma string de números: ')
    count = 0
    new_array = ''
    while count < len(array):
        if int(array[count]) % 2 == 0:
            new_array += '0'
        else:
            new_array += '1'
        count += 1
    print(new_array)


def get_number_str(msg):
    number_str = input(msg)
    while number_check(number_str) == False:
        print('A string deve conter apenas números.')
        number_str = input(msg)
    return number_str


def number_check(string):
    count = 0
    while count < len(string):
        if ord(string[count]) < 48 or ord(string[count]) > 57:
            return False
        count += 1
    return True



main()
