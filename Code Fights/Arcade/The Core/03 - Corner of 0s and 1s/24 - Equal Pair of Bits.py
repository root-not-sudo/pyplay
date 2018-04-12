def equalPairOfBits(n, m):
    return ~(n ^ m) & -~(n ^ m)


print(equalPairOfBits(10, 11))
print(equalPairOfBits(0, 0))
print(equalPairOfBits(28, 27))
print(equalPairOfBits(895, 928))
print(equalPairOfBits(1073741824, 1006895103))
