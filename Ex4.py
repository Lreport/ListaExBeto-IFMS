def characterCounter(text):
    word = text.replace(',','').replace('.', '').replace(';', '').replace(':', '').replace('!', '').replace('?', '').lower()
    return len(word)
print('Character Counter')
text = input('Enter the text: ')
print(f'The number of words in the text is: {characterCounter(text)}')