def main():
    for c in range(int(input())):
        rajesh, sheldon = input().split()
        print(game(rajesh, sheldon))

    
def game(rajesh, sheldon):
    if rajesh == 'tesoura':
        if sheldon == 'papel' or sheldon == 'lagarto':
            return 'rajesh'
        elif rajesh == sheldon:
            return 'empate'
        else:
            return 'sheldon'
    elif rajesh == 'papel':
        if sheldon == 'pedra' or sheldon == 'spock':
            return 'rajesh'
        elif rajesh == sheldon:
            return 'empate'
        else:
            return 'sheldon'
    elif rajesh == 'pedra':
        if sheldon == 'lagarto' or sheldon == 'tesoura':
            return 'rajesh'
        elif rajesh == sheldon:
            return 'empate'
        else:
            return 'sheldon'
    elif rajesh == 'lagarto':
        if sheldon == 'spock' or sheldon == 'papel':
            return 'rajesh'
        elif rajesh == sheldon:
            return 'empate'
        else:
            return 'sheldon'
    else:
        if sheldon == 'pedra' or sheldon == 'tesoura':
            return 'rajesh'
        elif rajesh == sheldon:
            return 'empate'
        else:
            return 'sheldon'


main()
