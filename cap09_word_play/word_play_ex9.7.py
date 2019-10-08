def main():
    fin = open('words.txt')
    for line in fin:
        if is_triple(line):
            print_line(line)
            


def print_line(string):
    for i in range(0, len(string)-1):
        print(string[i], end='')
    print()

    
def is_triple(word):
    triple = 0
    i = 0
   # for i in range(0, len(word)-1):
    while i < len(word)-1:
        if word[i] == word[i+1]:
            triple += 1
            i += 1
            if triple == 3:
                return True
        else:
            triple = 0
        i += 1
    return False





if __name__ == "__main__":
    main()