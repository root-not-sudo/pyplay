def willYou(young, beautiful, loved):

    return (young+beautiful+loved == 2) or (loved > young and loved > beautiful)


# better:
'''def willYou(young, beautiful, loved):
    return loved != (young and beautiful)'''
