def additionWithoutCarrying(param1, param2):
    n, sum = 0, 0
    while(param1 > 0 or param2 > 0):
        sum += (((param1 % 10) + (param2 % 10)) % 10)*10**n
        param1 //= 10
        param2 //= 10
        n += 1
    return sum


print(additionWithoutCarrying(456, 1734))  # 1180
print(additionWithoutCarrying(99999, 0))  # 99999
print(additionWithoutCarrying(999, 999))  # 888
print(additionWithoutCarrying(0, 0))  # 0
print(additionWithoutCarrying(54321, 54321))  # 8642
