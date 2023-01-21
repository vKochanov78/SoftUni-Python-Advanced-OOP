def read_matrix_func():
    rows, columns = map(int, input().split(', '))
    read_matrix = []

    for row in range(rows):
        row_data = list(map(int, input().split(' ')))
        read_matrix.append(row_data)

    return read_matrix


def sum_matrix_columns():
    matrix = read_matrix_func()
    rows = len(matrix)
    columns = len(matrix[0])

    column_sum = []

    for i in range(columns):
        current_sum = 0
        for j in range(rows):
            current_sum += matrix[j][i]

        column_sum.append(current_sum)

    return column_sum


matrix = sum_matrix_columns()
for i in matrix:  # i = Column sum
    print(i)
