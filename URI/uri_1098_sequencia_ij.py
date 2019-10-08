def main():
   i = 0
   j = 1
   impressionI = 0
   while i <= 2:
        if is_decimal(i):
           print('I={:.1f}'.format(i), end = ' ') 
        else:
           print('I={}'.format(int(i)), end = ' ')
        if is_decimal(j):
           print('J={:.1f}'.format(j)) 
        else:
           print('J={}'.format(int(j))) 
        j += 1 
        impressionI += 1
        if j >= 4 and impressionI >= 3:
           i += 0.2
           j = 1 + i
           impressionI = 0


def is_decimal(number):
    if int(number) == 2:
        return False
    elif (number*10)%10 != 0:
        return True
    else:
        return False
       
        
main()


# print('I={}'.format(int(i)), end = ' ') if ((i*10) % 10) == 0 else print('I={:.1f}'.format(i), end = ' ')
# print('J={}'.format(int(i))) if ((j*10) % 10) == 0 else print('j={:.1f}'.format(i))