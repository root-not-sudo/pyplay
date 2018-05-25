def isMAC48Address(inputString):

    if len(inputString) != 17:
        return False
    a = inputString.split('-')
    if len(a) != 6:
        return False
    for x in a:
        try:
            int(x, 16)
        except ValueError:
            return False
    return True
