def longestDigitsPrefix(inputString):

    s = ''
    if inputString[0] in '0123456789':
        for i in range(len(inputString)):
            if inputString[i] in '0123456789':
                s += inputString[i]
            else:
                break
    return s
