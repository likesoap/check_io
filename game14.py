def index_power(array: list, N: int):
    sum = 1
    if 0 < N < 100 and N <= len(array)-1:
        for i in range(N):
            sum *= array[N]
            i += 1
        return sum

    elif len(array) >= 1 and N == 0:
        return 1

    elif N > len(array)-1 and len(array) > 0:
        return -1


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    # assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    # assert index_power([0, 1], 0) == 1, "Zero power"
    # assert index_power([1, 2], 3) == -1, "IndexError"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    index_power([96, 92, 94], 3)
