def buildPalindrome(st):
    count, newst = 0, st
    while newst != newst[::-1]:
        newst = st + st[count::-1]
        count += 1
    return newst


print(buildPalindrome("abaa"))
