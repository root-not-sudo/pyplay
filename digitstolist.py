import math


def digitstolist(n):

    r = []
    order = math.floor(math.log10(n)) + 1
    for i in range(order):
        r.insert(0, n % 10)
        n = n // 10
    return r


def listtodigits(a):

    r = 0
    for i in range(len(a)):
        r += a[i] * 10**(len(a)-i-1)
    return r


print(digitstolist(100))
print(listtodigits([1, 2, 0, 9]))
