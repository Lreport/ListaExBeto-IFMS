def mean(notes:float):
    
    return sum(notes) / len(notes)

notes = []

try:
    n = int(input('Put number of notes: '))
    for i in range(1, n + 1):
        notes.append(float(input(f'Put note {i}: ')))
except ValueError:
    print('Please set a integer number.')

mean = mean(notes)
notesUpmean = [note for note in notes if note > mean]
if len(notesUpmean) < 2:
    print(f'The note above the mean is: {notesUpmean}')
else:
    print(f'The notes above the mean are: {notesUpmean}')

#print(f'Notas up mean: {notesUpmean}')