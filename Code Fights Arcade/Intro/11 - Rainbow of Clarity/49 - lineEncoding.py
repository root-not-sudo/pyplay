def lineEncoding(s):

    if len(set(s)) == len(s):
        return s
    else:
        s, g = s + ' ', ''
        counter = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            else:
                if counter == 0:
                    g = g + s[i-1]
                else:
                    g = g + str(int(counter + 1)) + s[i-1]
                counter = 0
        return g


# 2nd (top used regex)
'''from itertools import groupby
def lineEncoding(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x
'''

print(lineEncoding("aabbbc"))
print(lineEncoding("abbcabb"))
