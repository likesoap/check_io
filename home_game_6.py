def all_the_same(input: list):
    all_good = True
    for i in input:
        if not i == input[0]:
            all_good = False
    return all_good

    # for i in range(len(input)):
    #     while input[0] != input[i]:
    #         return False


print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']))
print(all_the_same([]))
