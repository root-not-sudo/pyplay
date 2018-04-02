import numpy


def spiralNumbers(n):

    a = numpy.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            a[i][j] = i*n + j + 1
    return a


print(spiralNumbers(6))
