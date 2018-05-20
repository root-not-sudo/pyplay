from math import sqrt, ceil


def rectangleRotation(a, b):

    a = ceil(a/sqrt(2))
    b = ceil(b/sqrt(2))
    c = a*b+(a-1)*(b-1)
    if c % 2 == 0:
        return c-1
    else:
        return c
