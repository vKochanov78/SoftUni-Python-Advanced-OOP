clothes = [int(n) for n in input().split()]
space_for_rack = int(input())

racks_count = 1

current_rack_space = space_for_rack

while clothes:
    cloth = clothes.pop()

    if current_rack_space - cloth >= 0:
        current_rack_space -= cloth

    else:
        racks_count += 1
        current_rack_space = space_for_rack - cloth

print(racks_count)