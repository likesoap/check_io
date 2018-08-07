import re


def is_stressful(string_input: str):
    the_matches = re.compile(
        r'h+.?e+.?l+.?p+.?|a+.?s+.?a+.?p+|\!+.?\!+.?\!+$|u+.?r+.?g+.?e+.?n+.?t+.?', re.I)
    if the_matches.search(string_input) != None:
        return True
    elif string_input.isupper() is True:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    print(is_stressful('Hi'))
    print(is_stressful('I neeeedd HELP'))
    print(is_stressful('h!e!l!p'))
    print(is_stressful('Heeeeeey!!! I’m having so much fun!'))
