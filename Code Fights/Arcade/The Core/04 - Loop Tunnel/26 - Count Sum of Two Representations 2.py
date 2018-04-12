def countSumOfTwoRepresentations2(n, l, r):
    A, B, count = l, r, 0
    if(l + r < n):
        A = n - B
    if(l + r > n):
        B = n - A
    while(A <= B):
        if (A + B == n):
            count += 1
        A += 1
        B -= 1
    return count


# better:
'''def countSumOfTwoRepresentations2(n, l, r):
    s = 0
    for i in range(l, r + 1):
        if i <= n - i <= r:
            s += 1
    return s'''


print(countSumOfTwoRepresentations2(6, 2, 4))  # 2
print(countSumOfTwoRepresentations2(6, 3, 3))  # 1
print(countSumOfTwoRepresentations2(10, 9, 11))  # 0
print(countSumOfTwoRepresentations2(24, 8, 16))  # 5
print(countSumOfTwoRepresentations2(24, 12, 12))  # 1
print(countSumOfTwoRepresentations2(93, 24, 58))  # 12
