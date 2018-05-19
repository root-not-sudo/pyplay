'''from math import log10, floor


def pagesNumberingWithInk(current, numberOfDigits):
    order = floor(log10(current)) + 1
    numberOfDigits -= order
    while numberOfDigits >= order:
        numberOfDigits -= order
        current += 1
        order = floor(log10(current)) + 1
    return current
'''


def pagesNumberingWithInk(current, numberOfDigits):
    while numberOfDigits >= len(str(current)):
        numberOfDigits -= len(str(current))
        current += 1
    return current-1


print(pagesNumberingWithInk(8, 4))
