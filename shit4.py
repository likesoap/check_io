import string

set1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
# a = string.ascii_lowercase
# # for i in a:
# #     print(i + ' has the codepoint: ' + str(ord(i)))


def set_new_set(input: set):
    new_set = set()
    for j in set1:
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


def compare(candidate: set, refer1: set, refer2: set):
    final_set = set()
    for m in refer1:
        if m in candidate:
            final_set.add(m)

    for n in refer2:
        if n in candidate:
            final_set.add(n)
    print(len(final_set))
    print(final_set)
    return(len(final_set))


# hop_left(set1)
# hop_right(set1)
compare(set_new_set(set1), hop_left(set1), hop_right(set1))
