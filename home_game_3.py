def checkio(text: list):
    text_1 = []
    for i in text:
        if text.count(i) > 1:
            text_1.append(i)
    return text_1


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    # assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    # assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    # assert list(checkio([10, 9, 10, 10, 9, 8])) == [
    #     10, 9, 10, 10, 9], "4th example"
    # checkio([10, 9, 10, 10, 9, 8])
    print(checkio([1, 2, 3, 4, 5]))
