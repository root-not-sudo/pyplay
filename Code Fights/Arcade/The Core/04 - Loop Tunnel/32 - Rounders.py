import math


def rounders(value):

    order = math.floor(math.log10(value)) + 1
    for i in range(1, order):
        if value % 10 < 5:
            value = value // 10
        else:
            value = value // 10 + 1
    return value * 10 ** (order - 1)


print(rounders(15))
print(rounders(1234))
print(rounders(1445))
print(rounders(14))
print(rounders(10))
print(rounders(99))
