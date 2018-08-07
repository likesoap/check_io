import string


def set_new_set(input: set):
    new_set = set()
    for j in input:
        row = int(j[1])
        col = ord(j[0])
        new_set.add((col, row))
    # print(new_set)
    return(new_set)


def hop_left(input: set):

    new_input = set()

    for k in input:
        row = int(k[1])+1
        col = ord(k[0])-1
        new_input.add((col, row))
    # print(new_input)
    return(new_input)


def hop_right(input: set):

    new_input = set()

    for l in input:
        row = int(l[1])+1
        col = ord(l[0])+1
        new_input.add((col, row))
    # print(new_input)
    return(new_input)


def safe_pawns(candidate: set):
    candidate_set = set_new_set(candidate)
    final_set = set()
    for m in hop_left(candidate):
        if m in candidate_set:
            final_set.add(m)

    for n in hop_right(candidate):
        if n in candidate_set:
            final_set.add(n)
    # print(len(final_set))
    # print(final_set)
    return(len(final_set))


# hop_left(set1)
# hop_right(set1)
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
