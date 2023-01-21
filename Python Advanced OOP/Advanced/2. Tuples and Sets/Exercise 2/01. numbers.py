first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

functions_map = {
    'Add First': lambda x: [first.add(num) for num in x],
    'Add Second': lambda x: [second.add(num) for num in x],
    'Remove First': lambda x: [first.discard(num) for num in x],
    'Remove Second': lambda x: [second.discard(num) for num in x],
    'Check Subset': lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False),
}

for _ in range(int(input())):
    first_command, *data = input().split()
    command = first_command + " " + data.pop(0)

    if data:
        functions_map[command]([int(x) for x in data])
    else:
        functions_map[command]()

print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')
