def switchLights(a):

    summation = sum(a)
    if summation > 0:
        for i in range(len(a)):
            if a[i] == 1:
                if summation % 2 != 0:
                    a[i] = 0
                summation -= 1
            elif a[i] == 0 and summation % 2 != 0:
                a[i] = 1
    return a
