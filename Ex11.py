def wordCounter(text):
    word = text.replace(',','').replace('.', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '').lower()
    return len(word.split())
print('Word Counter')
text = (input('Enter the text: '))
print(f'The number of words in the text is: {wordCounter(text)}')