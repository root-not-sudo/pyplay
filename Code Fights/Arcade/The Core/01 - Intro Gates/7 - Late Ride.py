def lateRide(n):

    a, b = str(n//60) + str(n % 60), 0
    for i in a:
        b += int(i)

    return b
