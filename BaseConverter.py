"""recursive base conversion, not functioning yet"""


def baseConverter(num, base):
    if (num == 0):
        return 0
    else:
        return baseConverter(num / base, base) + (num % base)


print(baseConverter(99, 2))  # 1100011
