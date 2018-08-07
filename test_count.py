import string


def checkio(text):
    """
    We iterate through latin alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


print(checkio('asdfiasdfujpasdufas98d7uf089a7fd897uasd0fahsdkhtyqp6thkhbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbgajlhbapjhfdpasdf'))
