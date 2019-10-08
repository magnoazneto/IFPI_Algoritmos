def main():
    for case in range(int(input())):
        words = input().split()
        words.sort(key = len, reverse = True)
        print(' '.join(words))
    

main()
