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


# 2nd (top was stupid regex):
'''def isMAC48Address(inputString):
    try:
        all = inputString.split('-')
        if len(all) != 6:
            return False
        for s in all:
            if len(s) != 2:
                return False
            int(s, 16)
        return True
    except:
        return False'''


print(isMAC48Address("02-03-04-05-06-07"))
