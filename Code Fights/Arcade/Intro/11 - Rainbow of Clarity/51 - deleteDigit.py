import math
import itertools


def deleteDigit(n):

    a = []
    forder = math.floor(math.log10(n))
    b = digitstolist(n)
    r = itertools.combinations(b, forder)
    for i in r:
        a.append(listtodigits(i))
    return max(a)


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



# top
'''def deleteDigit(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))'''

print(deleteDigit(10))
