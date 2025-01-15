#def isNegative(n):
    #return n < 0
def factorial(n:int, i=2):
  if n == 1:
    return
  if n % i == 0:
    print(i)
    factorial(n // i, i)
  else:
    factorial(n, i + 1)
try:
    n = int(input('Put a integer number: '))
    if n < 0:
       print('Error. The number must be positive.')
    elif n == 0:
        print(f'The factorial of {n} is: 1')
    elif n == 1:
        print(f'The factorial of {n} is: 1')
    else:
        print(f'The factorial of {n} is:')
        factorial(n)
except ValueError:
    print('Please set a integer number.')