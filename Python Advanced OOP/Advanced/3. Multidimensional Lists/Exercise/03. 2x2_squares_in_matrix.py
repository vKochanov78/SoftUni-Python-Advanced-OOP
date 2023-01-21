rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
squares_count = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_symbol = matrix[row][col]

        if matrix[row][col + 1] == current_symbol and \
            matrix[row + 1][col] == current_symbol and \
            matrix[row + 1][col + 1] == current_symbol:

            squares_count += 1

print(squares_count)
