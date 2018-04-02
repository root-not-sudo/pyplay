def circleOfNumbers(n, firstNumber):

    m = n/2
    if firstNumber < m:
        return firstNumber + m
    else:
        return firstNumber - m
