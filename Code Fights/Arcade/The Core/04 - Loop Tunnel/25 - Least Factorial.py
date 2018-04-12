def leastFactorial(n):
    m, i = 1, 1
    while m < n:
        m *= i
        i += 1
    return m


print(leastFactorial(17))
print(leastFactorial(1))
print(leastFactorial(5))
