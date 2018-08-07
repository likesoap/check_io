def most_frequent(array: list):
    list_dict = {}
    final_array = []
    for i in array:
        if i in list_dict.keys():
            list_dict[i] += 1
        else:
            list_dict.setdefault(i, 0)
    final_array = sorted(list_dict, key=list_dict.__getitem__, reverse=True)
    return final_array[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
