def checkio(array: str):
    array1 = array.split()
    while 0 < len(array1) < 100 and len(array1)-2 >= 1:
        for i in range(len(array1)-2):
            if array1[i].isalpha() and array1[i+1].isalpha() and array1[i+2].isalpha():
                return True
            return False
    return False


if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    # print(checkio("Hello World hello"))
    # print(checkio("He is 123 man"))
    # print(checkio("1 2 3 4"))
    # print(checkio("bla bla bla bla"))
    # print(checkio("Hi"))
