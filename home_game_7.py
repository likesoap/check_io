import string


def to_encrypt(input: str, digit: int):
    input = list(input.lower())
    reference = string.ascii_lowercase*abs(digit)
    # print(reference)
    for i in range(len(input)):
        if input[i] in reference:
            input[i] = reference[reference.find(input[i])+digit]
    print(''.join(input))


if __name__ == '__main__':
    to_encrypt("a b c", 3)
    to_encrypt("a b c", -3)
    to_encrypt("simple text", 16)
    to_encrypt("important text", 10)
    to_encrypt("state secret", -13)
