def main():
    begin = 10
    while begin <= 1000:
        if is_prime(begin):
            print(begin, end = ' ')
        begin += 1
    print()


def is_prime(num):
    i = 2
    divisores = 2
    while i <= (num ** (1/2)):
        if num % i == 0:
            divisores += 1
        if divisores > 2: break
        i += 1
    if divisores <= 2:
        return True
    else:
        return False



main()
