def main():
    fin = open('words.txt')
    for line in fin:
        if len(line)-1 > 20:
            print_line(line)

        
def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()


if __name__ == '__main__':
    main()
