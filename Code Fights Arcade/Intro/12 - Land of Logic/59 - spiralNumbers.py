import numpy


def spiralNumbers(n):

    a, i, j, k, end = numpy.zeros(shape=(n, n)), 0, -1, 0, n*n
    while k < end:
        # right
        while j < n - i - 1:
            j, k = j+1, k+1
            a[i][j] = k

        # down
        while i < j:
            i, k = i+1, k+1
            a[i][j] = k

        # left
        while j > n - i - 1:
            j, k = j-1, k+1
            a[i][j] = k

        # up
        while i > j + 1:
            i, k = i-1, k+1
            a[i][j] = k

    return a


print(spiralNumbers(3))
print(spiralNumbers(6))
