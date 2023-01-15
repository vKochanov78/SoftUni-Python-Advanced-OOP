numbers = tuple(map(float, input().split()))

number_counter = {}

for num in numbers:
    if num not in number_counter:
        number_counter[num] = 0
    number_counter[num] += 1

for k, v in number_counter.items():
    print(f"{k} - {v} times")