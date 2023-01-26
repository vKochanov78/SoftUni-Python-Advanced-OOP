size = int(input())
matrix = [[int(n) for n in input().split()] for _ in range(size)]

command = input().split()
while command[0] != "END":
    current_command, row, col, val = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")

    elif current_command == "Add":
        matrix[row][col] += val
    elif current_command == "Subtract":
        matrix[row][col] -= val

    command = input().split()

[print(*row) for row in matrix]

