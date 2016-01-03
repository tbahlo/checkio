def weak_point(matrix):
    row_durabilities = []
    for row in matrix:
        rowsum = 0
        for current_value in row:
            rowsum += current_value
        row_durabilities.append(rowsum)

    column_durabilities=[]
    for column in range(0, len(matrix[0])):
        columnsum = 0
        for row in range(0,len(matrix)):
            columnsum += matrix[row][column]
        column_durabilities.append(columnsum)

    minrow = row_durabilities.index(min(row_durabilities))
    mincolumn = column_durabilities.index(min(column_durabilities))

    return minrow, mincolumn  # [0, 0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
