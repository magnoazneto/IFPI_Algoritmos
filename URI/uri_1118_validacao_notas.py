def main():
   nota1 = validacao(float(input()))
   nota2 = validacao(float(input()))
   media = (nota1+nota2)/2
   print('media = {:.2f}'.format(media))
   print('novo calculo (1-sim 2-nao)')
   opc = valida_opc(int(input()))
   if opc == 1:
      main()
   else:
      pass


def valida_opc(opc):
   while opc not in range(1, 3):
      print('novo calculo (1-sim 2-nao)')
      opc = int(input())
   return opc

   
def validacao(nota):
   while nota < 0 or nota > 10:
      print('nota invalida')
      nota = float(input())
   return nota
   


main()
