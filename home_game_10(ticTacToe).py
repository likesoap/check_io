def check_row(row1: str, row2: str, row3: str):
    if row1.count(row1[0]) == len(row1) and row1[0] == 'X':
        return 'X'
    elif row1.count(row1[0]) == len(row1) and row1[0] == 'O':
        return 'O'
    elif row2.count(row2[0]) == len(row2) and row2[0] == 'X':
        return 'X'
    elif row2.count(row2[0]) == len(row2) and row2[0] == 'O':
        return 'O'
    elif row3.count(row3[0]) == len(row3) and row3[0] == 'X':
        return 'X'
    elif row3.count(row3[0]) == len(row3) and row3[0] == 'O':
        return 'O'
    else:
        return 'D'


def check_col(row1: str, row2: str, row3: str):
    for m in range(3):
        if row1[m] == row2[m] == row3[m] == 'X':
            return 'X'
        elif row1[m] == row2[m] == row3[m] == 'O':
            return 'O'
    return 'D'


def check_diag(row1: str, row2: str, row3: str):
    if row1[0] == row2[1] == row3[2] == 'X':
        return 'X'
    elif row1[0] == row2[1] == row3[2] == 'O':
        return 'O'
    elif row1[2] == row2[1] == row3[0] == 'X':
        return 'X'
    elif row1[2] == row2[1] == row3[0] == 'O':
        return 'O'
    else:
        return 'D'


def checkio(input: str):
    row1 = []
    row2 = []
    row3 = []

    for i in input[0]:
        row1.append(i)

    for k in input[1]:
        row2.append(k)

    for l in input[2]:
        row3.append(l)

    print('check row= '+check_row(row1, row2, row3))
    print('check col= '+check_col(row1, row2, row3))
    print('check diag= '+check_diag(row1, row2, row3))

    if check_row(row1, row2, row3) == 'X' or check_col(row1, row2, row3) == 'X' or check_diag(row1, row2, row3) == 'X':
        return 'X'
    elif check_row(row1, row2, row3) == 'O' or check_col(row1, row2, row3) == 'O' or check_diag(row1, row2, row3) == 'O':
        return 'O'
    else:
        return 'D'

    # assert checkio([
    #     "X.O",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins"
    # assert checkio([
    #     "OO.",
    #     "XOX",
    #     "XOX"]) == "O", "Os wins"
    # assert checkio([
    #     "OOX",
    #     "XXO",
    #     "OXX"]) == "D", "Draw"
    # assert checkio([
    #     "O.X",
    #     "XX.",
    #     "XOO"]) == "X", "Xs wins again"
# print(checkio([
#     "OOX",
#     "XXO",
#     "OXX"]))
# print(checkio([
#     "OO.",
#     "XOX",
#     "XOX"]))


print(checkio([".O.", "XXX", ".O."]))
