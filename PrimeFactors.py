import math

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = int(n / 2)
    sqrt_n = int(math.sqrt(n) // 1)
    i = 3
    while i <= sqrt_n:
        if n % i == 0:
            factors.append(i)
            n = int(n / i)
        else:
            i += 2

    if n != 1:
        factors.append(n)
    return factors


import math


def prime_factors_boot_dev(n):
    prime_factors = []
    while n % 2 == 0:
        n /= 2
        prime_factors.append(2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n /= i
            prime_factors.append(i)
    if n > 2:
        prime_factors.append(int(n))
    return prime_factors


print(prime_factors(2197))
print(prime_factors_boot_dev(2197))
