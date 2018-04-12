'''a = '00000000' + bin(2567447)[2:]
print(a)
print(int(a[len(a)-8:len(a)], 2))
print(int(a[len(a)-16:len(a)-8], 2))
print(int(a[len(a)-24:len(a)-16], 2))


def arrayPacking(a):
    b = '000000000000000000000000' + bin(2567447)[2:]
    return([int(b[len(b)-24:len(b)-16], 2), int(b[len(b)-16:len(b)-8], 2), int(b[len(b)-8:len(b)], 2)])'''


def arrayPacking(a):
    r = ''
    for i in range(len(a)-1, -1, -1):
        r = r + bin(a[i])[2:].zfill(8)
    return int(r, 2)


# top:
'''def arrayPacking(a):

    p = 0

    for q in reversed(a):
        p = p << 8
        p = p | q

    return p'''


'''def arrayPacking(a):
    return sum([a[i] << i*8 for i in range(len(a))])'''


print(arrayPacking([24, 85, 0]))
