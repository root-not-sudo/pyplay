def houseOfCats(legs):

    if legs % 4 == 0:
        return list(range(0, legs//2 + 1, 2))
    else:
        return list(range(1, legs//2 + 1, 2))
