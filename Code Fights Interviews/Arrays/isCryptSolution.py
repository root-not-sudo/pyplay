def isCryptSolution(crypt, solution):

    b = []
    for i in range(len(crypt)):
        k = ''
        for j in crypt[i]:
            for d in solution:
                if d[0] == j:
                    k = k + d[1]
        if k[0] == '0' and len(k) > 1:
            return False
        b.append(k)

    return int(b[0]) + int(b[1]) == int(b[2])


print(isCryptSolution(["SEND",
                       "MORE",
                       "MONEY"], [["O", "0"],
                                  ["M", "1"],
                                  ["Y", "2"],
                                  ["E", "5"],
                                  ["N", "6"],
                                  ["D", "7"],
                                  ["R", "8"],
                                  ["S", "9"]]))


print(isCryptSolution(["A",
                       "A",
                       "A"], [["A", "0"]]))

print(isCryptSolution(["AA",
                       "AA",
                       "AA"], [["A", "0"]]))


print(isCryptSolution(["BAA",
                       "CAB",
                       "DAB"], [["A", "0"],
                                ["B", "1"],
                                ["C", "2"],
                                ["D", "4"]]))
