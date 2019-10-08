def main():
    msg = input()
    print('Mensagens alteradas:', identify_mars(msg))


def identify_mars(string):
    default = 'HELP'
    lenght = len(default)
    i = 0
    def_idx = 0
    infected_msgs = 0
    while i < len(string):
        if string[i] == default[def_idx]:
            def_idx += 1
            i += 1
            if def_idx == 4:
                def_idx = 0
        else:
            infected_msgs += 1
            i += lenght - def_idx
            def_idx = 0
    return infected_msgs


main()