def pairsNumbers(integers:int):
    return [num for num in integers if num % 2 == 0]
integers = []
try:
    n = int(input('Put number of integers: '))
    for i in range(1, n + 1):
        integers.append(int(input(f'Put integer {i}: ')))
except ValueError:
    print('Please set a integer number.')
print(f'The pairsnumber integers is: {pairsNumbers(integers)}')