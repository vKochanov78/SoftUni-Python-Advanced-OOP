matrix = []
rover_pos = []
SIZE = 6

for row in range(SIZE):
    line = input().split()
    if "E" in line:
        rover_pos = [row, line.index("E")]

    matrix.append(line)

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

deposits = {
    "W": 0,  # water
    "M": 0,  # metal
    "C": 0,  # concrete
}

deposits_full_name = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}

commands = input().split(", ")
for direction in commands:
    rover_pos[0] = directions[direction][0] + rover_pos[0]
    rover_pos[1] = directions[direction][1] + rover_pos[1]

    for i in range(len(rover_pos)):
        if rover_pos[i] < 0:
            rover_pos[i] = SIZE - 1
        elif rover_pos[i] == SIZE:
            rover_pos[i] = 0

    current_position = matrix[rover_pos[0]][rover_pos[1]]

    if current_position in deposits:
        print(f"{deposits_full_name[current_position]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        deposits[current_position] += 1
    elif current_position == "R":
        print(f"Rover got broken at ({rover_pos[0], rover_pos[1]})")
        break

if all(deposits.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony")