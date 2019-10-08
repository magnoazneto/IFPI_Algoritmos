from get_inputs import get_inteiro
def main():
    valor = get_inteiro('Fatorial de quanto? ')
    print(fatorial(valor))


def fatorial(valor):
   fatorial = 1
   for i in range(valor, 0, -1):
      fatorial *= i
   return fatorial
   

main()