def main():
    for c in range(0, int(input())):
        fibonacci = [0, 1]
        parada = int(input())
        for c in range(0, parada):
            fibonacci.append(fibonacci[c]+fibonacci[c+1])
        termo = fibonacci[parada]
        print('Fib({}) = {}'.format(parada, termo))
         

main()
