def second_index(text,symbol):
    if text.count(symbol)<2:
        return None
    first = text.find(symbol,0)
    second = text.find(symbol, first+1)
    return second


if __name__ == '__main__':
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')