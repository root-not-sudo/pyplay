def integerToStringOfFixedWidth(number, width):
    num = str(number)
    length = len(num)
    if(length >= width):
        return str(num[length-width:length])
    else:
        return '0'*(width - length) + num


print(integerToStringOfFixedWidth(1234, 2))
print(integerToStringOfFixedWidth(1234, 4))
print(integerToStringOfFixedWidth(1234, 5))
print(integerToStringOfFixedWidth(0, 1))
print(integerToStringOfFixedWidth(89, 4))
print(integerToStringOfFixedWidth(23456, 4))
print(integerToStringOfFixedWidth(89, 3))

'''def integerToStringOfFixedWidth(number, width):
    return str(number).zfill(width)[-width:]'''
