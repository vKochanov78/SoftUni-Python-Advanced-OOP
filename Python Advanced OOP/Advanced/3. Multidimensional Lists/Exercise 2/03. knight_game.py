size = int(input())
matrix = [list(input()) for _ in range(size)]

directions = {
    (-2, -1),  # top left
    (-1, -2),  # left up
    (1, -2),  # left down
    (-2, 1),  # top right
    (-1, 2),  # right up
    (1, 2),  # right down
    (2, -1),  # bottom left
    (2, 1),  # bottom right
}

knights_removed = 0

while True:
    max_attacks = 0
    knights_with_most_attacks_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in directions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1
                if max_attacks < attacks:
                    knights_with_most_attacks_position = [row, col]
                    max_attacks = attacks

    if max_attacks:
        r, c = knights_with_most_attacks_position
        matrix[r][c] = '0'
        knights_removed += 1
    else:
        break
print(knights_removed)