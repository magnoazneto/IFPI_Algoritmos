def main():
    while True:
        try:
            text = input()
            dancing_text(text)
        
        except EOFError:
            break


def dancing_text(text):
    uppercase = True
    dancing = ''
    for char in range(0, len(text)):
        if is_letter(text[char]) and uppercase:
            #print(text[char].upper(), end='')
            dancing += text[char].upper()
            uppercase = False
        elif is_letter(text[char]):
            #print(text[char].lower(), end='')
            dancing += text[char].lower()
            uppercase = True
        else:
            #print(text[char], end='')
            dancing += text[char]
    print(dancing)


def is_letter(char):
    codigo = ord(char)
    return codigo >= 65 and codigo <= 90 or codigo >= 97 and codigo <= 122


main()
