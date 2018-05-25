def isCaseInsensitivePalindrome(inputString):

    inputString = inputString.lower()
    return inputString[0:-(-len(inputString)//2)] == inputString[:(-len(inputString)//2)-1:-1]


'''or just return inputString == inputString[::-1]'''
