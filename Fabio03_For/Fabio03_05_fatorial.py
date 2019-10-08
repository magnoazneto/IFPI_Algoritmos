from utilidades import get_inteiro
def main():
    valor = get_inteiro('Fatorial de quanto? ')
    print(fatorial(valor))


def fatorial(valor):
   fatorial = 1
   while valor > 0:
      fatorial *= valor
      valor -=1
   return fatorial
   

main()