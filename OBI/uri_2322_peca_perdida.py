def main():
    pecas_totais = int(input())
    pecas_encontradas = list(map(int, input().split()))
    print(lost_piece(pecas_totais, pecas_encontradas))


def lost_piece(pecas_totais, pecas_encontradas):
    for piece in range(1, pecas_totais+1):
        if not my_in(piece, pecas_encontradas):
            return piece


def my_in(elemento, conjunto):
    for i in range(len(conjunto)):
        if conjunto[i] == elemento:
            return True
    return False


main()
