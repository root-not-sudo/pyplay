def digitDegree(n):

    count = 0
    s = n
    while s > 9:
        s = sum_digits(s)
        count += 1
    return count


def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r
