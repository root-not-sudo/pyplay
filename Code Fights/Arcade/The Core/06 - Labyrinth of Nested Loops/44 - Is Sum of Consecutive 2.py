def isSumOfConsecutive2(n):
    if n == 1:
        return 0
    count = 0
    if n % 2 != 0:
        count = 1

    for j in range(1, n//2+1):
        sum = 0
        for i in range(j, n//2+1):
            sum += i
            if sum == n:
                count += 1
    return count


for i in range(25):
    print(i+1, '=', isSumOfConsecutive2(i+1))
