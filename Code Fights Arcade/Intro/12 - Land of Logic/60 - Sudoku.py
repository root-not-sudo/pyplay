def sudoku(grid):

    m = 0
    for b in grid:
        if len(b) != len(set(b)):
            return False
        p = []
        for n in range(9):
            p.append(grid[n][m])
        if len(p) != len(set(p)):
            return False
        m += 1

    for k in range(3):
        for i in range(3):
            p = []
            for j in range(3):
                p.append(grid[3*i][j+k*3])
                p.append(grid[3*i+1][j+k*3])
                p.append(grid[3*i+2][j+k*3])
            if len(p) != len(set(p)):
                return False

    return True


print(sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [1, 2, 3, 4, 5, 6, 7, 8, 9],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4]]))
