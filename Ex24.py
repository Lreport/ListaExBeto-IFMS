def invertedWord(word):
    return word[::-1]
word = input('Enter a word: ')
word = word.lower()
wordPalindrome = invertedWord(word)
if word == wordPalindrome:
    print(f'The word {word} is a palindrome.')
else:
    print(f'The word {word} is not a palindrome.')