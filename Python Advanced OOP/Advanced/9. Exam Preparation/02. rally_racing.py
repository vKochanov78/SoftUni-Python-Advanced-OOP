def create_matrix_func(size):
    result = []

    for row in range(size):
        line = input().split()
        result.append(line)

        if "T" in line:
            t_position.append([row, line.index("T")])

    return result


size = int(input())
racing_number = input()

# Finish statement.
is_finished = False

# Variable to count kms of the car.
passed_kms = 0

# There will be two nested lists with position of up - tunnel and down - tunnel.
t_position = []

# Directions the car can go.
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

# Position of our car.
car_position = [0, 0]

# The function which creates the race track(matrix).
matrix = create_matrix_func(size)

while True:
    command = input()

    if command == "End":
        matrix[car_position[0]][car_position[1]] = "C"
        break

    direction = command

    row = car_position[0] + directions[direction][0]
    col = car_position[1] + directions[direction][1]

    if matrix[row][col] == ".":
        passed_kms += 10
        car_position = [row, col]

    elif matrix[row][col] == "T":
        matrix[row][col] = "."
        car_position = [row, col]

        # If car position == first tunnel.
        if [row, col] == t_position[0]:

            row = t_position[1][0]
            col = t_position[1][1]
            car_position = [row, col]

        # If car position == second tunnel.
        else:

            row = t_position[0][0]
            col = t_position[0][1]
            car_position = [row, col]

        matrix[row][col] = "."
        passed_kms += 30
        continue

    elif matrix[row][col] == "F":
        is_finished = True
        passed_kms += 10

        matrix[row][col] = "C"
        car_position = [row, col]
        break

if is_finished:
    print(f"Racing car {racing_number} finished the stage!")
else:
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {passed_kms} km.")

for row in matrix:
    print(''.join(row))