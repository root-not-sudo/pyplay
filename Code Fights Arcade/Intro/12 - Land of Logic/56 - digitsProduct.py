def digitsProduct(product):
    if product == 0:
        return 10
    elif product < 10:
        return product
    else:
        a = stupid_factors(product)
        print(a)
        if max(a) > 9:
            return -1
        return listtodigits(a)


def stupid_factors(n):
    i = 9
    factors = []
    while i > 1:
        if n % i:
            i -= 1
        else:
            n //= i
            factors.insert(0, i)
    if n > 1:
        factors.append(n)
    return factors


def listtodigits(a):

    r = 0
    for i in range(len(a)):
        r += a[i] * 10**(len(a)-i-1)
    return r


print(digitsProduct(567))
print(digitsProduct(56))
print(digitsProduct(100))
