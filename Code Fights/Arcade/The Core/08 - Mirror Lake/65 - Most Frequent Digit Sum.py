from collections import Counter


def mostFrequentDigitSum(n):

    if n == 0:
        return 0
    funct = []
    while n > 0:
        r = 0
        m = n
        while m >= 1:
            r += m % 10
            m = m // 10
        funct.append(r)
        n -= r

    maximum = [0, 1]
    for i in Counter(funct).most_common():
        if i[0] > maximum[0] and i[1] >= maximum[1]:
            maximum = [i[0], i[1]]
    return maximum[0]


print(mostFrequentDigitSum(17))
