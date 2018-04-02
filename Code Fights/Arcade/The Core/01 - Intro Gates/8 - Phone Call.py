def phoneCall(min1, min2_10, min11, s):

    mins, b = 0, s
    while b > 0:
        if b == s and s-min1 >= 0:
            b -= min1
            mins += 1
        elif b >= min2_10 and mins < 10:
            b -= min2_10
            mins += 1
        elif b >= min11 and mins >= 10:
            b -= min11
            mins += 1
        else:
            break

    return mins


# top
'''def phoneCall(min1, min2_10, min11, s):
    if s<min1:
        return 0
    elif s>=min1 and s<=min1+9*min2_10:
        return 1+(s-min1)//min2_10
    return 10+(s-min1-9*min2_10)//min11'''


print(phoneCall(3, 1, 2, 20))
