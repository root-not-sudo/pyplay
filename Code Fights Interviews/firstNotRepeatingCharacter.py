from collections import Counter


def firstNotRepeatingCharacter(s):
    counter = Counter(s)
    for i in s:
        if counter.get(i) == 1:
            return i

    return '_'


# top
'''def firstNotRepeatingCharacter(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_''''


print(firstNotRepeatingCharacter("abaccabadd"))
