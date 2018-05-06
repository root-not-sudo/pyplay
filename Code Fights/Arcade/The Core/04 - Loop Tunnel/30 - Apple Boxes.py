def appleBoxes(k):
    yellow, red = 0, 0
    for i in range(k+1):
        if i % 2 == 0:
            red += i ** 2
        else:
            yellow += i ** 2

    return red - yellow


# more mathematical
'''def appleBoxes(n):
    return ((-1)**n)*n*(n+1)/2'''
