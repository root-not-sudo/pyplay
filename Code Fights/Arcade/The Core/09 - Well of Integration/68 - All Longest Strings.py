def allLongestStrings(inputArray):

    maxstrlen, outputarray = 0, []
    for i in inputArray:
        if len(i) > maxstrlen:
            outputarray = []
            maxstrlen = len(i)
        if len(i) == maxstrlen:
            outputarray.append(i)
    return outputarray
