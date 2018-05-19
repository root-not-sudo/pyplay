def factors(value):
    factorlist = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factorlist.append((i, int(value / i)))
    return factorlist


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(factors(39))
print(prime_factors(210))
