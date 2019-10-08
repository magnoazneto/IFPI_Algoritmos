def main():
    for c in range(int(input())):
        codigo = input()
        print(decodificar(codigo))


def decodificar(msg):
    count = 0
    new_str = ''
    while count < len(msg):
        if ord(msg[count]) >= 97 and ord(msg[count]) <= 122:
            new_str += msg[count]
        count += 1
    return new_str[::-1]



main()
