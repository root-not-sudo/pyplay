def electionsWinners(votes, k):

    winners, maxcounter, top = 0, 0, max(votes)
    for i in votes:
        if k == 0 and i == top:
            maxcounter += 1
        elif i + k > top:
            winners += 1

    if maxcounter > 1:
        return 0
    elif k == 0:
        return 1
    else:
        return winners


print(electionsWinners([1, 3, 3, 1, 1], 0))
