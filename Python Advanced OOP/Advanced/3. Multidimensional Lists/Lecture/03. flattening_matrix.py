def read_matrix_func():
    rows = int(input())
    read_matrix = []

    for current_row in range(rows):
        row = list(map(int, input().split(', ')))
        read_matrix.append(row)

    return read_matrix


def flattening_matrix_func():
    matrix = read_matrix_func()
    flattened_matrix = []

    for row in matrix:
        for num in row:
            flattened_matrix.append(num)

    return flattened_matrix


matrix = flattening_matrix_func()
print(matrix)
