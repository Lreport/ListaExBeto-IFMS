def sum_num(x:int, y:int):
    n = x + y
    return n
try:
    print('Sum of two numbers')
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    print(f'The sum  {x} + {y} = {sum_num(x, y)}')
except ValueError:
    print('Please set a integer number.')