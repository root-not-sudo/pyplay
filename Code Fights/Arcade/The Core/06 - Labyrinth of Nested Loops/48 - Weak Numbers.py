def weakNumbers(n):
    divisors = []
    for i in range(1, n+1):
        divisors.append(factors(i))
    weakness = []
    for i in range(1, n+1):
        weak = 0
        for j in range(1, i):
            if divisors[i-1] < divisors[j-1]:
                weak += 1
        weakness.append(weak)
    return [max(weakness), weakness.count(max(weakness))]


def factors(value):
    factorlist = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factorlist.append(i)
            if int(value / i) not in factorlist:
                factorlist.append(int(value / i))
    return len(factorlist)


print(weakNumbers(1000))
print(factors(499))
