def zigzag(a):
    counter = 0
    maximus = []
    if len(a) == 2:
        if a[0] == a[1]:
            return 1
        else:
            return 2
    for i in range(1, len(a)-1):
        if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
            counter += 1
        else:
            counter += 2
            maximus.append(counter)
            counter = 0
    return max(maximus)
