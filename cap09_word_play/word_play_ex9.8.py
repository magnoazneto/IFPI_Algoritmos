def main():
    for i in range(100000, 1000000):
        if bigger_palyndrome(str(i)):
            print(i)
   # string = input("Digite a palavra:\n>> ")
   # bigger = bigger_palyndrome(string)
   # if bigger:
   #     print(bigger)
   # else:
   #     print('Não achei.')


def bigger_palyndrome(string): # procura pelo maior palindromo
    len_string = len(string)
    count = 0
    for i in range(0, len(string)-1):
        while count <= i:
            sub_str = substring(string, count, len_string+count)
            if is_palindrome(sub_str):
                return sub_str
            count += 1
        count = 0
        len_string -= 1
    return False
        

def is_palindrome(word):  # verifica se uma paravra é um palíndromo
    return True if word == reverse_string(word) else False


def substring(string, inicio, fim):  # devolve uma substring entre os índices
    nova_string = ''
    while inicio < fim:
        nova_string += string[inicio]
        inicio += 1
    return nova_string


def reverse_string(str1): # [::-1]
    count = len(str1) - 1
    reverse_str = ''
    while count >= 0:
        reverse_str += str1[count]
        count -= 1
    return reverse_str


if __name__ == "__main__":
    main()