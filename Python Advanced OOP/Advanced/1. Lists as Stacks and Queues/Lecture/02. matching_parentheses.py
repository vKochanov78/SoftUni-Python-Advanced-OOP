data = input()

indices = []

for i in range(len(data)):
    current_char = data[i]

    if current_char == "(":
        indices.append(i)

    elif current_char == ")":
        last_index = indices.pop()

        print(data[last_index:i + 1])