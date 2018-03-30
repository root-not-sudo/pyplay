def avoidObstacles(inputArray):
    if inputArray == []:
        return 1

    opposite = []
    for i in range(1, max(inputArray)+2):
        if not(i in inputArray):
            opposite.append(i)

    inputArray.sort()
    for i in inputArray[::-1]:
        for j in opposite[::-1]:
            if (i % j == 0):
                opposite.remove(j)

    return opposite[0]
