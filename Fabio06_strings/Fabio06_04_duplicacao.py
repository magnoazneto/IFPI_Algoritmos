def main():
    string = input()
    string = double_chars(string)
    print(string)


def double_chars(string):
    count = 0
    new_str = ''
    while count < len(string):
        new_str += string[count]
        new_str += string[count]
        count += 1
    return new_str


main()
