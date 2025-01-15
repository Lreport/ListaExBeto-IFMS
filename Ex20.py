def FibonacciSequence(n:int):
    if n <= 1:
        return n
    else:
        return FibonacciSequence(n - 1) + FibonacciSequence(n - 2)
try:
    n = int(input('Put a integer number: '))
    print(f'The Fibonacci sequence of {n} is: {FibonacciSequence(n)}')
except ValueError:
    print('Please set a integer number.')