def main():
    while True:
        try:
            words = input().lower().split('-')
            test = 'cobol'
            bug = False
            index = 0
            while index <= 4:
                if words[index][0] == test[index] or words[index][-1] == test[index]:
                    index += 1
                else:
                    bug = True
                    break
                
            print('BUG' if bug else 'GRACE HOPPER')
            
        except EOFError:
            break
        

'''
def grace_tester(words):
    tester = ''
    if len(words) < 1: return False
    word = 'cobol'
    cobol_index = 0
    for w in words:
        if w[0] == word[cobol_index]:
            tester += w[0]
            cobol_index += 1
            if cobol_index > 4:
                return True if tester == 'cobol' else False
        if w[-1] == word[cobol_index]:
            tester += w[-1]
            cobol_index += 1
            if cobol_index > 4:
                return True if tester == 'cobol' else False
    return False '''


main()
