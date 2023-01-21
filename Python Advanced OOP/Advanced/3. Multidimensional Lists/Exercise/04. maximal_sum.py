rows, cols = map(int, input().split())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
the_biggest_square = []
max_sum = float('-inf')

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col: col+3]
        second_row = matrix[row+1][col: col+3]
        third_row = matrix[row+2][col: col+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            the_biggest_square = first_row, second_row,third_row
            max_sum = current_sum

print(f'Sum = {max_sum}')
[print(*the_biggest_square[row]) for row in range(3)]