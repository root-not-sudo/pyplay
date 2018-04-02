int matrixElementsSum(std::vector<std::vector<int>> matrix) {
    //matrix[row][col];
    int sum = 0;
    int col = matrix[0].size();
    int row = matrix.size();

    for (int i = 1; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (matrix[i-1][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            sum += matrix[i][j];
        }
    }

    return sum;
}
