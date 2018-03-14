def minesweeper(matrix):
    win = []
    ik = len(matrix) + 2
    jk = len(matrix[0]) + 2
# add zeros around the matrix
    matrix.insert(0, [0]*(jk))
    matrix.append([0]*(jk))
    for i in (range(1, ik-1)):
        matrix[i].insert(0, 0)
        matrix[i].append(0)

    print(matrix)

    for i in range(1, ik-1):
        win.append([])
        for j in range(1, jk-1):
            win[i-1].append(0)
            win[i-1][j-1] += sum([matrix[i+k][j+l] for k in [-1, 0, 1] for l in [-1, 0, 1]])
            win[i-1][j-1] -= matrix[i][j]

    return(win)


true = True
false = False
print(minesweeper([[true, false, false], [false, true, false], [false, false, false]]))
print(minesweeper([[false, false, false], [false, false, false]]))
print(minesweeper([[true, false, false, true], [
      false, false, true, false], [true, true, false, true]]))

#
# inter = 0
# inter += False
# inter += True
# inter += True
# print(inter)
