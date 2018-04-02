def validTime(time):

    a = time.split(':')
    return((0 <= int(a[0]) < 24) and (0 <= int(a[1]) < 60))


print(validTime("23:59"))
