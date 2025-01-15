def CelsiusToFahrenheit(C:float):
    F = C * 1.8 + 32
    return F
try:
    print('Temperature converter')
    C = float(input('Set the temperature in Celsius: '))
    print(f'The tempetature in Celsius to Fahreinheit is: {CelsiusToFahrenheit(C)}')
except ValueError:
    print('Please set a correct temperature valuer.')