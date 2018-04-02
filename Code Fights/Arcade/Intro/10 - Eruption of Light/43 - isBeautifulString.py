from collections import Counter


def isBeautifulString(inputString):

    count = Counter(inputString)
    max = count['a']
    for i in range(1, 26):
        if count[chr(ord('a')+i)] > max:
            return False
        max = count[chr(ord('a')+i)]

    return True


# top solution
'''import string
def isBeautifulString(inputString):

    r = [inputString.count(i) for i in string.ascii_lowercase]

    return r[::-1] == sorted(r)'''


print(isBeautifulString("aabbbcadfe"))
