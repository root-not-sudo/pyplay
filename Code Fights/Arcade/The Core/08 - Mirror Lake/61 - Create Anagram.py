from collections import Counter


def createAnagram(s, t):

    s_count = Counter(s)
    t_count = Counter(t)
    tot = 0
    for key in s_count:
        if s_count[key] - t_count[key] > 0:
            tot += s_count[key] - t_count[key]
    return tot
