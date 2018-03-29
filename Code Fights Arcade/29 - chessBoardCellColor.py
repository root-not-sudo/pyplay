def chessBoardCellColor(cell1, cell2):
    count = 0
    board = {}
    for ltrs in 'ABCDEFGH':
        count += 1
        for nums in '12345678':
            if count % 2 == 0:
                board[ltrs + nums] = 'dark'
            else:
                board[ltrs + nums] = 'light'
            count += 1

    print(board)
    return(board[cell1] == board[cell2])


print(chessBoardCellColor('A1', 'H3'))
