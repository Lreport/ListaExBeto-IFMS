def rectangleArea(b:float, l:float):
    area = b * l
    return area
try:
    b = float(input('Set the base: '))
    l = float(input('Set the length: '))
    print(f'The area of the rectangle is: {rectangleArea(b, l)}')
except ValueError:
    print('Please set a correct number.')