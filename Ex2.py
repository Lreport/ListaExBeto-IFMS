def evenNumber(n:int):
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")
try:
    n = int(input('Enter a number: '))
    evenNumber(n)
except ValueError:
    print('Please set a integer number.')