def correct_sentence(text):
    if not text.endswith('.'):
        text += '.'
    text = text[0].upper()+text[1:]
    return text

print(correct_sentence('Greetings, friend.'))

print(correct_sentence('greetings, friend.'))
print(correct_sentence('Greetings, friend'))
