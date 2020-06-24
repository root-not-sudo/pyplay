def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False

    return True


primes = []

for i in range(0, 1000000):
    if(isPrime(i)):
        print(i, ' is prime')
        primes.append(i)

if(17 in primes):
    print('we did it!')
