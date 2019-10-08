def main():
    cases = int(input())
    while (cases != 0):
        names = []
        bigger = 0
        for _ in range(cases):
            name = input()
            names += [name]
            if len(name) > bigger: bigger = len(name)

        for _ in range(cases):
            print(fill_with(names[_], ' ', bigger))

        cases = int(input())
        if cases == 0: break
        print()         


def fill_with(string, char, lenght):
    result = ''
    for _ in range(0, lenght - (len(string))):
        result += char
    return (result + string)


main()