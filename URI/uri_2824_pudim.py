def main():
    str1 = input()
    str2 = input()
    print(bigger_ordened_string(str1, str2))


def bigger_ordened_string(smaller, bigger):
    if len(smaller) > len(bigger):
        smaller, bigger = bigger, smaller
    target = ''
    idx_bigger = 0
    idx_smaller = 0
    checkpoint = 0
    while idx_smaller < len(smaller):
        while idx_bigger < len(bigger):
            if smaller[idx_smaller] == bigger[idx_bigger]:
                target += smaller[idx_smaller]
                idx_bigger += 1
                idx_smaller += 1
                if idx_smaller > len(smaller)-1:
                    break
                checkpoint = idx_bigger
            else:
                idx_bigger += 1
        idx_smaller += 1
        idx_bigger = checkpoint
    return len(target)
                


main()
