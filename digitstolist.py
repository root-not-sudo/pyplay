# takes an integer and turns it into a list with each element a single digit


def digitstolist(n):

    r = []
    while n >= 1:
        r.insert(0, n % 10)
        n = n // 10
    return r

# takes a list of single digit integers and turns it into a single base10 number


def listtodigits(a):

    r = 0
    for i in range(len(a)):
        r += a[i] * 10**(len(a)-i-1)
    return r

# takes a list of single binary numbers and turns it into a single base10 number


def binlisttodigits(a):

    r = 0
    for i in range(len(a)):
        r += a[i] * 2**(len(a)-i-1)
    return r


print(digitstolist(100))
print(listtodigits([1, 2, 0, 9]))
print(binlisttodigits(digitstolist(11111111)))
