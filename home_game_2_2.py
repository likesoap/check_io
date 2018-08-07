import string


def checkio(text: str):
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


if __name__ == '__main__':
    print(checkio("Lorem ipsum dolor sit amet 0000000000000000000"))
    print(checkio("Hello World!"))
    print(checkio("a-z"))
    print(checkio("12345,12345,12345 S 12345,12345"))
