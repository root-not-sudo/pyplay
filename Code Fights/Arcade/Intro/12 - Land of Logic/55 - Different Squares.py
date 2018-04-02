def differentSquares(matrix):

    a = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            b = matrix[i][j] + matrix[i+1][j]*10 + matrix[i][j+1]*100 + matrix[i+1][j+1]*1000
            a.append(b)

    return len(set(a))


print(differentSquares([[1, 2, 1], [2, 2, 2], [2, 2, 2], [1, 2, 3], [2, 2, 1]]))
print(differentSquares([[2, 5, 3, 4, 3, 1, 3, 2], [4, 5, 4, 1, 2, 4, 1, 3], [1, 1, 2, 1, 4, 1, 1, 5],  [1, 3, 4, 2, 3, 4, 2, 4],  [
      1, 5, 5, 2, 1, 3, 1, 1],  [1, 2, 3, 3, 5, 1, 2, 4],  [3, 1, 4, 4, 4, 1, 5, 5],  [5, 1, 3, 3, 1, 5, 3, 5], [5, 4, 4, 3, 5, 4, 4, 4]]))
