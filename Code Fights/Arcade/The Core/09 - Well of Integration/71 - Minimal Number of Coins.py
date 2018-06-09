def minimalNumberOfCoins(coins, price):

    coin_count = 0
    index = len(coins)-1
    while price > 0 and index >= 0:
        if price < coins[index]:
            index -= 1
        if price >= coins[index]:
            coin_count += 1
            price -= coins[index]
    return coin_count
