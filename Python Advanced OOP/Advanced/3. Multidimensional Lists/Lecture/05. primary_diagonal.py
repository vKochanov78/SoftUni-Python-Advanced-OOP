def read_matrix_func():
    rows = int(input())
    read_matrix = []

    for i in range(rows):
        row_data = list(map(int, input().split()))
        read_matrix.append(row_data)

    return read_matrix


def diagonal_sum_func():
    read_matrix = read_matrix_func()
    rows = len(read_matrix)
    sum_of_diagonal = 0

    for i in range(rows):
        sum_of_diagonal += read_matrix[i][i]

    return sum_of_diagonal


matrix = diagonal_sum_func()
print(matrix)

