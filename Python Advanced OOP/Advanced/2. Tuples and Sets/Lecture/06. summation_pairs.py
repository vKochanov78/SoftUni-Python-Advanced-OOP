numbers = list(map(int, input().split()))
target_number = int(input())

targets = set()
values_map = {}

for value in numbers:
    resulting_number = target_number - value
    targets.add(resulting_number)
    values_map[resulting_number] = value

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f"{pair} + {value} = {target_number}")

    else:
        resulting_number = target_number - value
        targets.add(resulting_number)
        values_map[resulting_number] = value

