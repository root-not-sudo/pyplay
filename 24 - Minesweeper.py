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

    for i in range(1, ik-1):
        win.append([])
        for j in range(1, jk-1):
            win[i-1].append(0)
            win[i-1][j-1] += sum([matrix[i+k][j+l] for k in [-1, 0, 1] for l in [-1, 0, 1]])
            win[i-1][j-1] -= matrix[i][j]

    return(win)

# top python


# def minesweeper(matrix):

#    r = []

#    for i in range(len(matrix)):
#        r.append([])
#        for j in range(len(matrix[0])):
#            l = -matrix[i][j]
#            for x in [-1, 0, 1]:
#                for y in [-1, 0, 1]:
#                    if 0 <= i+x < len(matrix) and 0 <= j+y < len(matrix[0]):
#                        l += matrix[i+x][j+y]

#            r[i].append(l)
#    return r


true = True
false = False
print(minesweeper([[true, false, false], [false, true, false], [false, false, false]]))
print(minesweeper([[false, false, false], [false, false, false]]))
print(minesweeper([[true, false, false, true], [
      false, false, true, false], [true, true, false, true]]))
