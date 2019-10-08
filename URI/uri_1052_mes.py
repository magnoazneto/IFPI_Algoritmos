def main():
    mes = int(input())
    print(filtra_mes(mes))


def filtra_mes(mes):
    if mes == 1:
        return 'January'
    elif mes == 2:
        return 'February'
    elif mes == 3:
        return 'March'
    elif mes == 4:
        return 'April'
    elif mes == 5:
        return 'May'
    elif mes == 6:
        return 'June'
    elif mes == 7:
        return 'July'
    elif mes == 8:
        return 'August'
    elif mes == 9:
        return 'September'
    elif mes == 10:
        return 'October'
    elif mes == 11:
        return 'November'
    else:
        return 'December'

main()