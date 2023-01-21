def read_matrix_func():
    rows = int(input())
    read_matrix = []

    for i in range(rows):
        row_data = list(input())
        read_matrix.append(row_data)

    return read_matrix


def find_symbol_in_matrix_func(read_matrix, special_symbol):
    for row in range(len(read_matrix)):
        for col in range(len(read_matrix[row])):
            current_symbol = read_matrix[row][col]
            if current_symbol == special_symbol:
                return row, col


def print_func(data, symbol):
    if data:
        print(data)
    else:
        print(f"{symbol} does not occur in the matrix")


matrix = read_matrix_func()
special_symbol = input()
print_func(find_symbol_in_matrix_func(matrix, special_symbol), special_symbol)

