def arrayMaxConsecutiveSum(inputArray, k):

    m = 0
    for j in range(k):
        m += inputArray[j]
    s = m
    for i in range(1, len(inputArray) - k+1):
        s = s + inputArray[i+k-1] - inputArray[i-1]
        if m < s:
            m = s
    return m


print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))
