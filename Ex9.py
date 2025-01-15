def ageVerify(age:int):
    if age >= 18:
        print('Accepted')
    else:
        print('Denied')
try:
    age = int(input('Enter your age: '))
except ValueError:
    print('Please set a integer number.')
ageVerify(age)