def differentRightmostBit(n, m):
    return (n ^ m) & -(n ^ m)


print(differentRightmostBit(11, 13))  # 2
print(differentRightmostBit(7, 23))  # 16, 5th bit
print(differentRightmostBit(1, 0))  # 1
print(differentRightmostBit(64, 65))  # 1
print(differentRightmostBit(1073741823, 1071513599))  # 131072, 18th bit
print(differentRightmostBit(42, 22))  # 4
