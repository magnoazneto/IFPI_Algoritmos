#import time
def main():
    while True:
        try:
            words = []
            smaller = ' '*50001
            for i in range(int(input())):
                word = input()
                words.append(word)
                if len(word) < len(smaller):
                    smaller = word
            #start = time.time()
            print(find_bigger(words, smaller))
            #end = time.time()
            #print(f'Tempo de execução: {(end-start):5.5f}')
        except EOFError:
            break
    

def find_bigger(words, smaller): # encontra o tamanho do maior palindromo
    bigger_palind = bigger_palyndrome(smaller)
    while bigger_palind and len(bigger_palind) > 1:
        #if in_all(bigger_palind, words):
        if all(bigger_palind in word for word in words):
            return len(bigger_palind)
        else:
            bigger_palind = bigger_palyndrome(bigger_palind[0:len(bigger_palind)-1])

  #  return len(intersection_sets(words))
    
    if is_anyone_there(smaller, words):
        return 1
    else:
        return 0


def intersection_sets(conjuntos):
    if len(conjuntos) == 1:
        return conjuntos
    else:
        return set(list(conjuntos[len(conjuntos)-1])) & set(list(intersection_sets(conjuntos[0:len(conjuntos)-1]))) 

'''
def is_anyone_there(smaller, words): # vefificar se ao menos 1 letra de smaller está presente em cada elemento de word
    for char in smaller:
        if in_all(char, words):
            return True
    return False
'''

def is_anyone_there(smaller, words): # vefificar se ao menos 1 letra de smaller está presente em cada elemento de word
    for char in smaller:
        if all(char in word for word in words):
            return True
    return False

'''
def in_all(target, words_list):  # verificar se o Target está presente em cada elemento de words_list
    for word in words_list:
        if set(target) & set(word) == 0:
            return False
    return True
'''
'''
def in_all(target, words_list):  # verificar se o Target está presente em cada elemento de words_list
    for word in words_list:
        if target not in word:
            return False
    return True
'''


def bigger_palyndrome(string): # procura pelo maior palindromo
    if len(string) == 1: return string
    len_string = len(string)
    count = 0
    for i in range(0, len(string)-1):
        while count <= i:
           # sub_str = substring(string, count, len_string+count)
            sub_str = string[count:len_string+count]
            if is_palindrome(sub_str):
                return sub_str
            count += 1
        count = 0
        len_string -= 1
    return False


def is_palindrome(word):  # verifica se uma paravra é um palíndromo
    return True if word == word[::-1] else False


main()
