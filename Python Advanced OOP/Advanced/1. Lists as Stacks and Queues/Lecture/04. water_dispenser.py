from _collections import deque

def add_people_to_deque():
    names = deque()

    while True:
        current_name = input()

        if current_name == COMMAND_START:
            break
        names.append(current_name)
    return names

COMMAND_END = "End"
COMMAND_START = "Start"
COMMAND_REFILL = "refill"

water_quantity = int(input())
people_deque = add_people_to_deque()

while True:
    command = input()

    if command == COMMAND_END:
        print(f"{water_quantity} liters left")
        break

    elif command.startswith(COMMAND_REFILL):
        refill_command_data = command.split()
        refill_water_amount = int(refill_command_data[1])
        water_quantity += refill_water_amount

    else:
        current_person = people_deque.popleft()
        current_litres = int(command)

        if current_litres <= water_quantity:
            print(f"{current_person} got water")
            water_quantity -= current_litres
        else:
            print(f"{current_person} must wait")

