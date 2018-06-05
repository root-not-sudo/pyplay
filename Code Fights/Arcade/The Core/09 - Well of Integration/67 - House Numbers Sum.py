def houseNumbersSum(inputArray):

    currentHouseNumbersSum, i = 0, 0
    while inputArray[i] != 0:
        currentHouseNumbersSum += inputArray[i]
        i += 1
    return currentHouseNumbersSum
