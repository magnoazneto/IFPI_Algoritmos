def main():
    pokemons = []
    for c in range(int(input())):
        pokemon = input()
        if pokemon not in pokemons:
            pokemons.append(pokemon)
    print('Falta(m) {} pomekon(s).'.format(151 - len(pokemons)))


main()
