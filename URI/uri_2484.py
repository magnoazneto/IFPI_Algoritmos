def main():
    while True:
        try:
            abracadabra(input())
        except EOFError:
            break 


def abracadabra(word):
    lenght = len(word)
    spaces = ''
    while lenght > 0:
        print(spaces, end = '')
        for l in range(0, lenght):
            if l < lenght-1:
                print(word[l], end = ' ')
            else:
                print(word[l])
        lenght -= 1
        spaces += ' '
    print()
        

main()
