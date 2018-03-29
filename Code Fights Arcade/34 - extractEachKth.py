def extractEachKth(inputArray, k):

    output = []
    for i in range(len(inputArray)):
        if not ((i+1) % k == 0):
            output.append(inputArray[i])

    return output
