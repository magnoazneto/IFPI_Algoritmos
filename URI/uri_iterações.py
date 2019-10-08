def main():
    i = 0
    j = 1
    printI = 0
    while i <= 2:
        if is_decimal(i) or is_decimal(j):
            while printI < 3:
                print('I={:.0f} J={:.0f}'.format(i, j+printI)) 
                printI += 1
        else:
            while printI < 3:
                print('I={:.1f} J={:.1f}'.format(i, j+printI))
                printI += 1
        printI = 0
        i += 0.2
        j += 0.2


def is_decimal(number):
    if number % 1 < 0.1:
        return True
    else:
        return False 
       
        
main()
