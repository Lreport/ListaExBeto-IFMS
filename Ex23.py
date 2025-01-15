def addition(x:float, y:float):
    return x + y
def subtraction(x:float, y:float):
    return x - y
def multiplication(x:float, y:float):
    return x * y
def division(x:float, y:float):
    return x / y
try:
    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))
except ValueError:
    print('Please set a correct number.')

print('1 - opration of addition')
print('2 - opration of subtraction')
print('3 - opration of multiplication')
print('4 - opration of division')
n = int(input('Enter your choice: '))
if n == 1:
    print(f'The result of addition is: {addition(x, y)}')
elif n == 2:
    print(f'The result of subtraction is: {subtraction(x, y)}')
elif n == 3:
    print(f'The result of multiplication is: {multiplication(x, y)}')
elif n == 4:
    print(f'The result of division is: {division(x, y)}')
else:
    print('Invalid choice')