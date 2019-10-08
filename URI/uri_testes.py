def main():
   i = 0
   j = 1
   impressionI = 0
   while i <= 2:
        if is_decimal(i):
           print('I={:.1f}'.format(i), end = ' ') 
        else:
           print('I={:.0f}'.format(i), end = ' ')
        if is_decimal(j):
           print('J={:.1f}'.format(j)) 
        else:
           print('J={:.0f}'.format(j)) 
        j += 1 
        impressionI += 1
        if j >= 4 and impressionI >= 3:
           i += 0.2
           aux = str(i)
           if float(aux[0:4]) == 1.99: i =  2
           j = 1 + i
           impressionI = 0


def is_decimal(number):
    if (number*10)%10 != 0:
        return True
    else:
        return False
       
        
main()
