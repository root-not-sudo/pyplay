def rangeBitCount(a, b):
    r = 0
    for i in range(a, b+1):
        r += countSetBits(i)
    return r


def countSetBits(n):

    if (n == 0):
        return 0
    else:
        return 1 + countSetBits(n & (n - 1))


# top
'''def rangeBitCount(a, b):
    return sum(bin(x).count('1') for x in range(a, b+1))'''


print(rangeBitCount(2, 5))
