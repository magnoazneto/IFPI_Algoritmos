def main():
    for case in range(int(input())):
        target = strip_str(input()).split()
        for word in target:
            print(word[0], end='')
        print()


def strip_str(text):  # corta todos os espaços extras de uma string
    if len(text) == 0: return ''
    previous_space = True
    count = 0
    new_str = ''
    while count < len(text):
        if (not previous_space or text[count] != ' '):
            new_str += text[count]
            if text[count] == ' ': 
                previous_space = True
            else:
                previous_space = False
        count +=1
    if len(new_str) > 0 and new_str[-1] == ' ': 
        new_str = string_pop(new_str, len(new_str)-1)   
    return new_str


def string_pop(string, index):  # remove um elemento da string pelo índice
    count = 0
    new_str = ''
    while count < len(string):
        if count != index:
            new_str += string[count]
        count += 1
    return new_str


main()