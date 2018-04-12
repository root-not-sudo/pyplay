def swapAdjacentBits(n):
    return (((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1))


print(swapAdjacentBits(13))
print(swapAdjacentBits(74))
print(swapAdjacentBits(1073741823))
print(swapAdjacentBits(0))
print(swapAdjacentBits(1))
print(swapAdjacentBits(83748))
