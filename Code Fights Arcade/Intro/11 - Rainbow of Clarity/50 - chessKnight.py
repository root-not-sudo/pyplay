def chessKnight(cell):

    moves = 4
    if cell[0] in 'ah' and cell[1] in '18':
        moves = 2
    elif (cell[0] in 'ah' and cell[1] in '27') or (cell[0] in 'bg' and cell[1] in '18'):
        moves = 3
    elif (cell[0] in 'bg' and cell[1] in '3456') or (cell[0] in 'cdef' and cell[1] in '27'):
        moves = 6
    elif cell[0] in 'cdef' and cell[1] in '3456':
        moves = 8

    return moves
