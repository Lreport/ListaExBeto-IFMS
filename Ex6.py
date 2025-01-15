def meanNotes(allNotes:float):
    MN = sum(allNotes) / len(allNotes)
    return MN
try:
    matter1 = float(input('Put Note 1: '))
    matter2 = float(input('Put Note 2: '))
    matter3 = float(input('Put Note 3: '))
    allNotes = matter1, matter2, matter3
except ValueError:
    print('Please set a correct number.')
print(f'The mean of notes is: {meanNotes(allNotes)}')