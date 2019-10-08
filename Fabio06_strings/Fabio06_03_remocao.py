def main():
    string = input('Digite uma frase: ')
    string = remove_all(string, ' ')
    print(string)


def remove_all(string, remove_char):
    count = 0
    new_str = ''
    while count < len(string):
        if string[count] != remove_char:
            new_str += string[count]
        count += 1
    return new_str
            

main()
