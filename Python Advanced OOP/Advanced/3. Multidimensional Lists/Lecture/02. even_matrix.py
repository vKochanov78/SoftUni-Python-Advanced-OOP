def read_matrix_func():
    rows = int(input())
    read_matrix = []

    for i in range(rows):
        row = input().split(', ')
        read_matrix.append(list(map(int, row)))

    even_matrices = [[x for x in row if x % 2 == 0] for row in read_matrix]

    return even_matrices

matrix = read_matrix_func()
print(matrix)
