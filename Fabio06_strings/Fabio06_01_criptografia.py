from string_tools import reverse_string, its_in
def main():
    string = input('Digite uma string: ')
    print(cript_str(string, '#'))


def cript_str(string, replace_char):
    string = reverse_string(string)
    count = 0
    new_string = ''
    while count < len(string):
        if its_in('AEIOUaeiou', string[count]):
            new_string += string[count]
        else:
            new_string += replace_char
        count += 1
    return new_string


main()
