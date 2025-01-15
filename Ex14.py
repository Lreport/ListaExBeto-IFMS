def invertedWord(word):
    return word[::-1]
word = input('Enter a word: ')
word = word.lower()
if word == invertedWord(word):
    print(f'The word {word} is a palindrome.')
else:
    print(f'The word {word} is not a palindrome.')