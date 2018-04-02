import math
import statistics as stats


def absoluteValuesSumMinimization(a):

    prob = math.floor(stats.median(a))
    nope = prob - 1
    sumprob = 0
    sumnope = 0
    for i in a:
        sumprob += abs(i - prob)
        sumnope += abs(i - nope)

    if (sumprob < sumnope):
        return prob
    else:
        return nope


print(absoluteValuesSumMinimization([-4, -1]))
