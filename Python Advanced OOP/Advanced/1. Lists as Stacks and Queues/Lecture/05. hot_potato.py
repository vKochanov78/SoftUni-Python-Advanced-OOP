from _collections import deque

names_of_players = input().split()
potato_step = int(input())

players_deque = deque(names_of_players)
counter = 0

while len(players_deque) > 1:
    counter += 1
    current_name_of_player = players_deque.popleft()

    if counter == potato_step:
        print(f"Removed {current_name_of_player}")
        counter = 0
    else:
        players_deque.append(current_name_of_player)

print(f"Last is {players_deque[0]}")

