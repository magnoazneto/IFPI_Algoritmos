from string_tools import get_string, substring
def main():
    time = get_string(len('hh:mm:ss'), 'Digite a hora no formato hh:mm:ss >> ')
    hora_certa(time)


def hora_certa(time):
    hour = substring(time, 0, 2)
    minutes = substring(time, 3, 5)
    seconds = substring(time, 6, 8)
    print('São %s hora(s), %s minuto(s) e %s segundo(s)' %(hour, minutes, seconds))


main()
