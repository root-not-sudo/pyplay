def squareDigitsSequence(a0):

    squareDigits = []
    element = a0
    while element not in squareDigits:
        squareDigits.append(element)
        print(squareDigits)
        i = 0
        while element >= 1:
            i += (element % 10) ** 2
            element = element // 10

        element = i
    return len(squareDigits)+1


print(squareDigitsSequence(1))
