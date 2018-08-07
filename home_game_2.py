def checkio(string: str):
    string = string.replace('!', ' ', -1).replace('?',
                                                  ' ', -1).replace('-', ' ', -1).replace(',', ' ', -1).lower()
    string1 = ''.join(string.split())
    # print(string1)
    string_dic = {}
    for y in range(len(string1)):
        if string1[y] in string_dic.keys() and not string1[y].isdecimal():
            string_dic[string1[y]] += 1
        elif not string1[y].isdecimal():
            string_dic.setdefault(string1[y], 1)
    # print(sorted(string_dic.items(), key=lambda x: x[1], reverse=True)[0])
    return(sorted(string_dic.items(), key=lambda x: (-x[1], x[0]))[0][0])


if __name__ == '__main__':
    # print("Example:")
    # print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing

    # checkio("Hello World!")
    # checkio("How do you do?")
    # checkio("One")
    # checkio("Oops!")
    # checkio("AAaooo!!!!")
    # checkio("abe")
    checkio("Lorem ipsum dolor sit amet 0000000000000000000")
    checkio("Hello World!")
    checkio("a-z")
    checkio("12345,12345,12345 S 12345,12345")
