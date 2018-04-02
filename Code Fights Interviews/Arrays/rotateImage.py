import numpy


def rotateImage(a):

    max = len(a)
    b = numpy.zeros(shape=(max, max))
    for i in range(max):
        for j in range(max):
            b[i][j] = a[max - j - 1][i]

    return b


print(rotateImage([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))
