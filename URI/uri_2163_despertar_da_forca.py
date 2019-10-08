def main():
    lines, colunms = map(int, input().split())
    matrix = []
    for i in range(lines):
        matrix.append(list(map(int, input().split())))

    result = seek_saber(matrix)
    if result != 0:
        print("%d %d" %(result[0]+1, result[1]+1))
    else:
        print("0 0")
    
    # for line in matrix:
    #     print(line)


def seek_saber(matrix):
    for line in range(1, (len(matrix))-1):
        for item in range(1, (len(matrix[line])-1)):
            if matrix[line][item] == 42:
                place = [line, item]
                if its_saber(place, matrix):
                    return place
                #print(place)
    return 0


def its_saber(place, matrix):
    # if place[0] == 0 or place[0] == (len(matrix))-1 or place[1] == (len(matrix[0])-1) or place[1] == 0:
    #     return False
    if signal_up(place, matrix):
        if signal_sides(place, matrix):
            if signal_down(place, matrix):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def signal_up(place, matrix):
    for signal in range(place[1]-1, place[1]+2):
        if matrix[place[0]-1][signal] != 7:
            return False
    return True


def signal_down(place, matrix):
    for signal in range(place[1]-1, place[1]+2):
        if matrix[place[0]+1][signal] != 7:
            return False
    return True


def signal_sides(place, matrix):
    if matrix[place[0]][place[1]-1] == 7 and matrix[place[0]][place[1]+1] == 7:
        return True
    else:
        return False
    
                

main()
