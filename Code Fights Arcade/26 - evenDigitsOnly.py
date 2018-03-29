def evenDigitsOnly(n):

    st = str(n)
    for i in st:
        if not int(i) % 2 == 0:
            return False
    return True


print(evenDigitsOnly(248622))
print(evenDigitsOnly(642386))
print(evenDigitsOnly(248842))
print(evenDigitsOnly(1))
print(evenDigitsOnly(8))
print(evenDigitsOnly(2462487))
print(evenDigitsOnly(468402800))
print(evenDigitsOnly(2468428))
print(evenDigitsOnly(5468428))
print(evenDigitsOnly(7468428))
