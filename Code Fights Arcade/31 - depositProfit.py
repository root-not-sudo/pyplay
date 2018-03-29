import math


def depositProfit(deposit, rate, threshold):

    t = math.log(threshold/deposit) / math.log(1 + rate/100)
    return math.ceil(t)


print(depositProfit(100, 20, 170))
