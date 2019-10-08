def main():
    i = 0
    j = 1
    printI = 0
    while i <= 2:
        if is_decimal(i) or is_decimal(j):
            print('I={:.1f} J={:.1f}'.format(i, j)) 
        else:
            print('I={:.0f} J={:.0f}'.format(i, j))
        j += 1 
        printI += 1
        if printI >= 3:
            i = ((i *10) + 2)/10
          #  aux = str(i)
          #  if float(aux[0:4]) == 1.99: i =  2
            j = 1 + i
            printI = 0


def is_decimal(number):
    if number % 1 < 0.1:
        return False
    else:
        return True
       
        
main()
