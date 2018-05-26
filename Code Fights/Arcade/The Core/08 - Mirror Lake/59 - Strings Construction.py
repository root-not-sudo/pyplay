from collections import Counter


def stringsConstruction(a, b):

    a_count = Counter(a)
    b_count = Counter(b)
    find_min = 500
    for key in a_count:
        if b_count[key]//a_count[key] <= find_min:
            find_min = b_count[key]//a_count[key]
    return find_min


# top:
'''def stringsConstruction(a, b):
    return min(b.count(c)//a.count(c) for c in a)'''
