def organizeNums():
    return sorted(nums)
nums = []
try:
    n = int(input('Put the number of quantity: '))
    if n < 0:
        print('Error. The number must be positive.')
    else:
        for i in range(1, n + 1):
            nums.append(int(input(f'Put the number {i}: ')))
    print(f'The numbers are: {organizeNums()}')
except ValueError:
    print('Please set a integer number.')