from string_tools import string_pop
def main():
    text = input()
    print(word_counter(strip_str(text)), 'palavra(s).')


def word_counter(text):
    words = 1
    count = 0
    while count < len(text):
        if text[count] == ' ':
            words += 1
        count += 1
    if len(text) == 0: words -= 1
    return words


def strip_str(text):
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

main()
