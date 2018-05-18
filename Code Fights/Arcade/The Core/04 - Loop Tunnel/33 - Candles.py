def candles(candlesNumber, makeNew):

    candles_burned = candlesNumber
    while candlesNumber >= makeNew:
        candles_burned += candlesNumber // makeNew
        candlesNumber = candlesNumber // makeNew + candlesNumber % makeNew
    return candles_burned


print(candles(5, 2))
