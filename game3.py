def first_word(text):
    text = text.replace('.',' ').replace(',',' ').strip()
    text = text.split()
    return text[0]

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print("Coding complete? Click 'Check' to earn cool rewards!")