def main():
    for c in range(int(input())):
        print('Prime' if is_prime(int(input())) else 'Not Prime')


def is_prime(num):
    if num > 2 and num % 2 == 0: return False # Fail Fast
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