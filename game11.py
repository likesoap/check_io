def checkio(array: list):
    addup = 0
    x = 0
    if not len(array) < 1:
        # for x in range(len(array)):
        while x <= len(array)-1:
            addup += array[x]
            x += 2
        return addup*array[-1]
    else:
        return 0


if __name__ == '__main__':
    # assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    # assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    # assert checkio([6]) == 36, "(6)*6=36"
    # assert checkio([]) == 0, "An empty array = 0"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print(checkio([0, 1, 2, 3, 4, 5]))
    print(checkio([1, 3, 5]))
    print(checkio([6]))
    print(checkio([]))
