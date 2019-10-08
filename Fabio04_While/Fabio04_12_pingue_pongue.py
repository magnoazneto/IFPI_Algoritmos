from utilidades import get_int_positivo
def main():
    vencedor = False
    player1 = player2 = 0
    while not vencedor:
        ponto = get_ponto('Pontuador:  ')
        if ponto == 1:
            player1 += 1
        else:
            player2 += 1
        print(f'PLACAR - Player 1: {player1} x {player2} Player 2')
        vencedor = partida(player1, player2)
    
    if player1 > player2:
        winner = 'Player 1'
    else:
        winner = 'Player 2'
    print('O vencedor foi:', winner)
    

def partida(player1, player2):
    if (player1 >= 21 and (player1-player2) >= 2)\
        or (player2 >= 21 and (player2-player1) >= 2):
        return True
    else:
        return False


def get_ponto(msg):
    ponto = get_int_positivo(msg)
    while ponto != 1 and ponto != 2:
        print('Jogador inválido.')
        ponto = get_int_positivo(msg)
    return ponto


main()
