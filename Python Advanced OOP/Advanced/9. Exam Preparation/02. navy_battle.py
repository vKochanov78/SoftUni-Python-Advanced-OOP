size = int(input())
submarine_coordinates = []
matrix = []

cruisers = 3
times_hit = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    line = list(input())
    matrix.append(line)

    if "S" in line:
        submarine_coordinates = [row, line.index("S")]
        matrix[row][submarine_coordinates[1]] = "-"

while cruisers:
    direction = input()

    row = directions[direction][0] + submarine_coordinates[0]
    col = directions[direction][1] + submarine_coordinates[1]

    submarine_coordinates = [row, col]

    if matrix[row][col] == "*":
        times_hit += 1

        if times_hit == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
            break

    elif matrix[row][col] == "C":
        cruisers -= 1

    matrix[row][col] = "-"

else:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[submarine_coordinates[0]][submarine_coordinates[1]] = "S"
[print(*row, sep="") for row in matrix]