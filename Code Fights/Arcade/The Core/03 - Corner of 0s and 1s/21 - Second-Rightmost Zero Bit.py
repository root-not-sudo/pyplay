def secondRightmostZeroBit(n):
    return ~(n | n + 1) & (n | n + 1)+1


print(secondRightmostZeroBit(37))
