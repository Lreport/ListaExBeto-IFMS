def vowelsCounter(text):
    text = text.lower()
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)
def consonantsCounter(text):
    return sum(1 for char in text if char.isalpha() and char not in 'aeiou')
text = input('Put the phrase: ')
vowels = vowelsCounter(text)
consonants = consonantsCounter(text)
print(f'The number of vowels is: {vowels}')
print(f'The number of consonants is: {consonants}')