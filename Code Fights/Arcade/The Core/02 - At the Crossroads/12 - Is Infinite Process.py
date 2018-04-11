def isInfiniteProcess(a, b):

    return False if a <= b and ((a % 2 == 0 and b % 2 == 0) ^ (a % 2 != 0 and b % 2 != 0)) else True
