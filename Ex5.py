def multiTable(n:int):
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')
try:
    n = int(input('Enter a number: '))
    print(f'the mulplicate table of {n} is = {multiTable(n)}')
except ValueError:
    print('Please set a integer number.')