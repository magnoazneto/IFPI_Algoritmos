def main():
    instalados, internet = map(int, input().split())
    installed_programs = make_array(instalados)
    for i in range(instalados):
        installed_programs[i] = list(map(int, input().split()))
    internet_programs = make_array(internet)
    for i in range(internet):
        internet_programs[i] = list(map(int, input().split()))

    upgrade_software(installed_programs, internet_programs)
    


def upgrade_software(installed_programs, internet_programs):
    upgraded = make_array(0)
    for i in range(len(installed_programs)):
        update_index = has_update(installed_programs[i], internet_programs)
        if update_index != False:
            upgraded = add_at_last(upgraded, internet_programs[int(update_index)])

    for software in range(len(upgraded)):
        print('%d %d' %(upgraded[software][0], upgraded[software][1]))   



def has_update(installed, internet_programs):
    bigger = 0
    update = False
    for i in range(len(internet_programs)):
        if internet_programs[i][0] == installed[0] and internet_programs[i][1] > installed[1]:
            bigger = i
            update = True
    if update:
        return str(bigger)
    else:
        return False

            


def make_array(lenght, value = 0):
    return [value] * lenght


def transfer(array1, array2):
    for i in range(len(array1)):
        array2[i] = array1[i]


def add_at_last(array, element):
    new_array = make_array(len(array)+1)
    transfer(array, new_array)
    new_array[len(new_array)-1] = element
    return new_array


main()
