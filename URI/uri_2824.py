def main():
    str1, str2 = input(), input()
    str1_list = list(str1)
    str2_list = list(str2)
    str1_list.sort()
    str2_list.sort()
    str1 = ''.join(str1_list)
    str2 = ''.join(str2_list)
    '''
    print('==='*8)
    print(str1)
    print(str2)  ''' 
    if len(str1) > len(str2):
        str1, str2 = str2, str1 
    str2 = get_disorder_sub(str1, str2)
   # print(str2)
    #str1 = get_disorder_sub(str1, str2)
    print(bigger_substr(str1, str2))
    

def bigger_substr(str_min, str_max):  # retorna o tamanho da maior substring comum entre 2 strings
    if str_min > str_max:
        str_min, str_max = str_max, str_min
    if str_min in str_max: return len(str_min)
    start = 0
    loop = 1
    extension = len(str_min) - loop
    while loop <= len(str_min):
        while start <= loop:
            sub_str = str_min[start:extension+start]
            if sub_str in str_max: return len(sub_str)
            start += 1
        loop += 1
        extension -= 1
        start = 0
    return 0


def get_disorder_sub(str1, str2):
    count = 0
    sub_str = ''
    while count < len(str2):
        if str2[count] in str1:
           # if str2[count] not in sub_str:
            sub_str += str2[count]
        count += 1
    return sub_str

 
main()