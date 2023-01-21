from collections import deque

bees_value = deque(int(x) for x in input().split())
nectar_value = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

functions_map = {
    '*': lambda x, y: abs(x * y),
    '/': lambda x, y: abs(x / y),
    '+': lambda x, y: abs(x + y),
    '-': lambda x, y: abs(x - y),
}

while bees_value and nectar_value:
    bee = bees_value.popleft()
    nectar = nectar_value.pop()

    if nectar < bee:
        bees_value.appendleft(bee)
    elif nectar > bee:
        total_honey += functions_map[symbols.popleft()](bee, nectar)

print(f"Total honey made: {total_honey}")

if bees_value:
    print(f"Bees left: {', '.join(str(x) for x in bees_value)}")

if nectar_value:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_value)}")
