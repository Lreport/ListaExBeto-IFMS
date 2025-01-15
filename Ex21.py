def NoDuplicate(integers:int):
    return list(set(integers))
integers = []

try:
    n = int(input('Put number of integers: '))
    for i in range(1, n + 1):
        integers.append(int(input(f'Put integer {i}: ')))
except ValueError:
    print('Please set a integer number.')

print(f'The number integers is: {NoDuplicate(integers)}')