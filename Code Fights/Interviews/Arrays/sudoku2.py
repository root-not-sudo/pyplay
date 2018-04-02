def sudoku2(grid):

    m = 0
    for b in grid:
        if len(b)-b.count('.') != len(set(b))-1:
            return False
        p = []
        for n in range(9):
            p.append(grid[n][m])
        if len(p)-p.count('.') != len(set(p))-1:
            return False
        m += 1

    for k in range(3):
        for i in range(3):
            p = []
            for j in range(3):
                p.append(grid[3*i][j+k*3])
                p.append(grid[3*i+1][j+k*3])
                p.append(grid[3*i+2][j+k*3])
            if len(p)-p.count('.') != len(set(p))-1:
                return False

    return True
