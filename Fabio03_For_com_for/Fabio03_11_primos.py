from get_inputs import get_inteiro
from math_utils import is_prime
def main():
    limite_sup = get_inteiro('Digite o limite superior: ')
    limite_inf = get_inteiro('Digite o limite inferior: ')
    for i in range(limite_inf, limite_sup+1):
        if is_prime(i): print(i, end = ' ')
    print()


main()