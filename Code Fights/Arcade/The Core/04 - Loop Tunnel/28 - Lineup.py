def lineUp(commands):
    turn, sameface = 0, 0
    for i in commands:
        if i == 'L' or i == 'R':
            turn += 1
        if turn % 2 == 0:
            sameface += 1
    return sameface


print(lineUp("LLARL"))
