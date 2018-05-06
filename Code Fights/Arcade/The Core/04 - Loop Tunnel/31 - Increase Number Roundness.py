def increaseNumberRoundness(n):
    while n % 10 == 0:
        n = n // 10
    while n >= 1:
        if n % 10 == 0:
            return True
        n = n // 10
    return False


# simpler:
'''def increaseNumberRoundness(n):
    return '0' in str(n).rstrip('0')'''
