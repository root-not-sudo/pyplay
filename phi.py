def phi(n, start):
    x = start
    for i in range(n):
        x = 1 + 1/x
        print(i, 'is', x)
    return 0


def sqrtpwr(n):
    x = 2**0.5
    for i in range(n):
        x = 2**(0.5 * x)
    return x


print(sqrtpwr(10**1))

# trying and failing to do: sqrt(1 + sqrt(2+ sqrt(3+ sqrt(4+ sqrt(5+ sqrt(6+ sqrt(7...)))))))


def sqrter(n):
    if n == 1:
        return 1
    else:
        return (n + sqrter(n-1))**0.5


print(sqrter(10))
