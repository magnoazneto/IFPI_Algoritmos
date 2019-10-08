def main():
    possiveis = 0
    for i in range(1, 30):
        num = fill(str(i), 2, '0')
        if int(num[::-1]) <= 80 and int(num) >= 13:
            print(num)
            possiveis += 1
            if possiveis == 6: break



def fill(string, lenght, char):
    new_str = string
    while len(new_str) < lenght:
        new_str = char + new_str
    return new_str 




if __name__ == "__main__":
    main()