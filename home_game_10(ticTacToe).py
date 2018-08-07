def check_row(row1: str, row2: str, row3: str):
    for n in row1:
        if row1[0] == n == 'X':
            return 'X'
        elif row1[0] == n == 'O':
            return 'O'
        else:
            return 'D'

    for n in row2:
        if row2[0] == n == 'X':
            return 'X'
        elif row2[0] == n == 'O':
            return 'O'
        else:
            return 'D'

    for o in row3:
        if row3[0] == o == 'X':
            return 'X'
        elif row3[0] == o == 'O':
            return 'O'
        else:
            return 'D'


def check_col(row1: str, row2: str, row3: str):
    for m in range(3):
        if row1[m] == row2[m] == row3[m] == 'X':
            return 'X'
        elif row1[m] == row2[m] == row3[m] == 'O':
            return 'O'
        else:
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

    check_row(row1, row2, row3)
    check_col(row1, row2, row3)
    check_diag(row1, row2, row3)



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
print(checkio([
    "X.O",
    "XX.",
    "XOO"]))
