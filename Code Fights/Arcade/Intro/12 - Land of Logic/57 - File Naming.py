def fileNaming(names):

    a = []
    k = 1
    for i in range(len(names)):
        if names[i] in a:
            k = 1
            while names[i] + '(' + str(k) + ')' in a:
                k += 1
            a.append(names[i] + '(' + str(k) + ')')
        else:
            a.append(names[i])

    return a


print(fileNaming(["a(2)", "a", "a(3)", "a", "a", "a(2)",
                  "a", "a(2)", "a(1)", "a", "a", "a", "a", "a", "a"]))
