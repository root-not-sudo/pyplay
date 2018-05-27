def numberOfClans(divisors, k):

    div = []
    for i in range(1, k+1):
        dip = ''
        for j in divisors:
            if i % j == 0:
                dip += '1'
            else:
                dip += '0'
        div.append(dip)

    return len(set(div))


print(numberOfClans([2, 3], 6))
print(numberOfClans([2, 3, 4], 6))
print(numberOfClans([1, 3], 10))
print(numberOfClans([6, 2, 2, 8, 9, 2, 2, 2, 2], 10))
