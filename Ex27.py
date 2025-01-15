import collections
import re

def mostFreqWord(text, n):
    text = re.sub(r'[^\w\s]', '', text)
    words = text.lower().split()
    counter = collections.Counter(words)
    return counter.most_common(n)
try:
    text = input('Enter the text: ')
    n = int(input('Enter the number of most frequent words: '))
    print(f'The {n} most frequent words in the text are: {mostFreqWord(text, n)}')
except ValueError:
    print('Please set a integer number.')