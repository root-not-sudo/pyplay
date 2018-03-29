import itertools


def stringsRearrangement(inputArray):
    p = itertools.permutations(inputArray)
    for j in p:
        allMatch = True
        for i in range(len(j) - 1):
            if not isDifferByOneChar(j[i], j[i + 1]):
                allMatch = False
                break
        if allMatch:
            return True
    return False


def isDifferByOneChar(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count == 1


print(stringsRearrangement(["ab", "bb", "aa"]))
