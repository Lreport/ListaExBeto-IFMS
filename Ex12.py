def primeNumbers():
    try:
        firstnum = int(input('Put the first number: '))
        lastnum = int(input('Put the last number: '))
    except ValueError:
        print('Please set a integer number.')

    def isPrime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [num for num in range(firstnum, lastnum + 1) if isPrime(num)]
    return primes

primes = primeNumbers()
print(f'The prime numbers between {primes[0]} and {primes[-1]} are: {primes}')