from _collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

number = int(input())

for _ in range(number):
    data = [int(x) for x in input().split()]
    map_functions[data[0]](data)

numbers.reverse()

print(*numbers, sep=", ")