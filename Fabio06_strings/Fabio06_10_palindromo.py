from string_tools import reverse_string
def main():
    word = lower(input())
    print('É palíndromo' if is_palindrome(word) else 'Não é palindromo.')


def is_palindrome(word):
    return True if word == reverse_string(word) else False


def lower(word):
    count = 0
    new_str = ''
    while count < len(word):
        if is_letter(word[count]):
            codigo = ord(word[count])
            if codigo >= 65 and codigo <= 90:
                new_str += chr(codigo + 32)
            else:
                new_str += word[count]
        else:
            new_str += word[count]
        count += 1
    return new_str


def is_letter(char):
    codigo = ord(char)
    if (codigo >= 65 and codigo <= 90) or (codigo >= 97 and codigo <= 122):
        return True
    else:
        return False




main()
