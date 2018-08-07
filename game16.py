def checkio(input: int):
    if 0 < input < 10**16:
        incre = 1
        input_str = str(input).replace('0', '1')
        for i in input_str:
            incre *= int(i)
    return incre


print(checkio(100023))
