def comfortableNumbers(l, r):
    numbs = []
    for i in range(l, r+1):
        temp = []
        j = i - s(i)
        while j <= i + s(i):
            if j > i and j <= r and i >= j - s(j) and i <= j + s(j):
                temp.append(j)
            j += 1
        numbs.append(temp)

    sum = 0
    for i in range(len(numbs)):
        sum += len(numbs[i])
    return sum


def s(num):
    sum = 0
    while num >= 1:
        sum += num % 10
        num = num // 10
    return sum


print(comfortableNumbers(1, 1000))
