import math


def messageFromBinaryCode(code):

    a, n = '', 8
    msg = [int(code[i:i+n]) for i in range(0, len(code), n)]
    for i in msg:
        a = a + chr(binlisttodigits(digitstolist(i)))

    return a


def digitstolist(n):

    r = []
    order = math.floor(math.log10(n)) + 1
    for i in range(order):
        r.insert(0, n % 10)
        n = n // 10
    return r


def binlisttodigits(a):

    r = 0
    for i in range(len(a)):
        r += a[i] * 2**(len(a)-i-1)
    return r


print(messageFromBinaryCode("010110010110111101110101001000000110100001100001011001000010000001101101011001010010000001100001011101000010000001100000011010000110010101101100011011000110111100101110"))
