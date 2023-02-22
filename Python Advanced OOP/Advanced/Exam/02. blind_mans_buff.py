n, m = map(int, input().split())
playground = []
player_pos = None
opponent_count = 0

for i in range(n):
    row = input().split()
    playground.append(row)
    if 'B' in row:
        player_pos = (i, row.index('B'))
    opponent_count += row.count('P')

moves_made = 0
opponents_touched = 0

while True:
    command = input()
    if command == 'Finish':
        break

    new_pos = None
    if command == 'up':
        new_pos = (player_pos[0]-1, player_pos[1])
    elif command == 'down':
        new_pos = (player_pos[0]+1, player_pos[1])
    elif command == 'left':
        new_pos = (player_pos[0], player_pos[1]-1)
    elif command == 'right':
        new_pos = (player_pos[0], player_pos[1]+1)

    if new_pos and 0 <= new_pos[0] < n and 0 <= new_pos[1] < m:
        target = playground[new_pos[0]][new_pos[1]]
        if target == '-':
            moves_made += 1
            playground[new_pos[0]][new_pos[1]] = 'B'
            playground[player_pos[0]][player_pos[1]] = '-'
            player_pos = new_pos
        elif target == 'P':
            opponents_touched += 1
            moves_made += 1
            playground[new_pos[0]][new_pos[1]] = '-'
            playground[player_pos[0]][player_pos[1]] = '-'
            player_pos = new_pos

    if opponents_touched == opponent_count:
        break

print('Game over!')
print(f'Touched opponents: {opponents_touched} Moves made: {moves_made}')