def tennisSet(s1, s2):

    return (s1 == 6 and s2 < 5) or (s2 == 6 and s1 < 5) or (s1 == 7 and 4 < s2 < 7) or (s2 == 7 and 4 < s1 < 7)
