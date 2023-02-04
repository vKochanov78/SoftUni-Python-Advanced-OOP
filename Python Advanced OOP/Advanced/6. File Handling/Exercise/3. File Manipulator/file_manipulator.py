import os


while True:
    command, *data = input().split("-")

    if command == "End":
        break

    if command == "Create":
        with open(f"{data[0]}", "w") as file:
            continue

    elif command == "Add":
        with open(f"{data[0]}", "a") as file:
            file.write(f"{data[1]}\n")

    elif command == "Replace":
        try:
            with open(f"{data[0]}", "r") as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(data[1], data[2])

            with open(f"{data[0]}", "w") as file:
                file.write("".join(text))

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(data[0])
        except FileNotFoundError:
            print("An error occurred")

