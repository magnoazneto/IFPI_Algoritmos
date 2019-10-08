def main():
    while True:
        try:
            str_min, str_max = input(), input()
            if len(str_min) > len(str_max):
                str_min, str_max = str_max, str_min
            print(bigger_substr(str_min, str_max))
    
        except EOFError:
            break


def bigger_substr(str_min, str_max):
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
    

main()
