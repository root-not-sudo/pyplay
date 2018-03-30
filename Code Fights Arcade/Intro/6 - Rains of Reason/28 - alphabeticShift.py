def alphabeticShift(inputString):

    outputString = ''
    for i in range(len(inputString)):
        if inputString[i] != 'z':
            outputString += chr(ord(inputString[i])+1)
        else:
            outputString += 'a'
    return outputString


print(alphabeticShift('inputStringZ'))
