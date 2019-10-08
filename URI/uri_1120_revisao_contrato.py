def main():
    while True:
        try:
            text = input()
            print(html(text))

        except EOFError:
            break


def html(text):
    new_str = ''
    italic_open = False
    bold_open = False
    for i in range(len(text)):
        if text[i] == '_':
            if italic_open:
                new_str += '</i>'
                italic_open = False
            else:
                new_str += '<i>'
                italic_open = True
        elif text[i] == '*':
            if bold_open:
                new_str += '</b>'
                bold_open = False
            else:
                new_str += '<b>'
                bold_open = True
        else:
            new_str += text[i]

    return new_str


main()
