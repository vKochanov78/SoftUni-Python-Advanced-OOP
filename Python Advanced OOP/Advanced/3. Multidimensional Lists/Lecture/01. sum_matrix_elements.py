def read_matrix_func():
    rows, columns = [int(x) for x in input().split(', ')]
    read_matrix = []

    for row in range(rows):
        read_matrix.append([int(x) for x in input().split(', ')])

    return read_matrix


def sum_of_the_matrix():
    read_matrix = read_matrix_func()
    rows = len(read_matrix)
    cols = len(read_matrix[0])
    column_sum = []

    for i in range(cols):
        matrix_sum = 0
        for m in range(rows):
            matrix_sum += read_matrix[m][i]

        column_sum.append(matrix_sum)

    total_sum = sum(int(x) for x in column_sum)

    return total_sum, read_matrix


matrix = sum_of_the_matrix()
print(matrix[0])  # Printing total_sum_of_columns
print(matrix[1])  # Printing matrix
