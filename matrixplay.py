import random
random.seed()


def random_matrix_generator(num_size, rows, cols):

    matrix = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(random.randrange(num_size))
        matrix.append(row)
    return matrix


def matrix_row_col_del(matrix, row, rowend, col, colend):

    del matrix[row:rowend]
    for i in range(len(matrix)):
        del matrix[i][col:colend]
    return matrix


# rows and columns as lists (not necessarily continuous)
def constructSubmatrix(matrix, rowsToDelete, columnsToDelete):

    if len(rowsToDelete) > 0:
        for i in rowsToDelete:
            del matrix[i]
    if len(columnsToDelete) > 0:
        for i in range(len(matrix)):
            del_counter = 0
            for j in columnsToDelete:
                del matrix[i][j - del_counter]
                del_counter += 1
    return matrix


a = random_matrix_generator(10, 20, 20)

for i in a:
    print(i)

print('\n')
b = matrix_row_col_del(a, 2, 12, 2, 12)

for i in b:
    print(i)
