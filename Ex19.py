def CharacterCounter(text):
    counter = {}
    for character in text:
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter
text = input('Enter the text: ')
print(f'The number of characters in the text is: {CharacterCounter(text)}')