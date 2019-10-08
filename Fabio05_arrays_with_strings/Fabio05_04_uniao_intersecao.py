def main():
    A = input()
    B = input()
    C = A + B
    D = intersecao(A, B)
    print('União: %s\nInterseção: %s' %(C, D))


def intersecao(str1, str2):
    count = 0
    count2 = 0
    intersec = ''
    while count < len(str1):
        while count2 < len(str2):
            if str1[count] == str2[count2]:
                if not(its_in(intersec, str1[count])):
                    intersec += str1[count]
            count2 += 1
        count += 1
        count2 = 0
    return intersec


def its_in(string, piece, begin= 0):
    if len(piece) > len(string): return False  # Fail fast
    len_substring = len(piece)
    limit = len(string) - len(piece)
    while begin <= limit:
        if substring(string, begin, begin + len_substring) == piece:
            return True
        begin += 1
    return False


def substring(string, inicio, fim):
    nova_string = ''
    while inicio < fim:
        nova_string += string[inicio]
        inicio += 1
    return nova_string
           



main()
