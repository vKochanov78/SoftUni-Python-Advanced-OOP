def move_func(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return  my_position

    if field[r][c] == "x":
        return my_position

    return [r, c]


def shoot_func(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == "x":
            field[r][c] = "."
            return [r, c]
        r += directions[direction][0]
        c += directions[direction][1]

size = 5
field = []
targets = 0
targets_hit = 0
targets_hit_positions = []
my_position = []
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    field.append(input().split())

    if "A" in field[row]:
        my_position = [row, field[row].index("A")]
        field[row][my_position[1]] = "."

    if "x" in field[row]:
        targets += field[row].count("x")

for _ in range(int(input())):
    command_data = input().split()

    if command_data[0] == "move":
        my_position = move_func(command_data[1], int(command_data[2]))
    elif command_data[0] == "shoot":
        target_down_position = shoot_func(command_data[1])

        if target_down_position:
            targets_hit_positions.append(target_down_position)
            targets_hit += 1

        if targets == targets_hit:
            print(f"Training completed! All {targets} targets hit.")
            break

else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep='\n')