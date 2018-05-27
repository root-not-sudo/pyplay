def numbersGrouping(a):

    a_order = []
    for i in a:
        a_order.append(-(-i//10000))
    return len(a) + len(set(a_order))


print(numbersGrouping([1, 10000]))
