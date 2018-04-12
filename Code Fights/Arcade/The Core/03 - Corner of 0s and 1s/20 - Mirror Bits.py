def mirrorBits(a):

    return int(bin(a)[:1:-1], 2)


print(mirrorBits(97))
