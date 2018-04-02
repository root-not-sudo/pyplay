def sumUpNumbers(inputString):
    a, count, max = [], 0, 0

    for i in range(len(inputString)):
        if i == len(inputString) - 1 and inputString[i] in '0123456789':
            a.append(int(inputString[count:i+1]))
        if inputString[i] not in '0123456789':
            if inputString[i-1] in '0123456789' and i != 0:
                a.append(int(inputString[count:i]))
            count = i + 1

    if count == 0:
        if len(inputString) > 0:
            return int(inputString)

    return sum(a)


print(sumUpNumbers("a100"))
