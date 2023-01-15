car_numbers_data = [input().split(", ") for _ in range(int(input()))]

parking_lot = set()

COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for direction, car_number_plate in car_numbers_data:
    if direction == COMMAND_IN:
        parking_lot.add(car_number_plate)

    elif direction == COMMAND_OUT:
        parking_lot.remove(car_number_plate)

if parking_lot:
    for current_plate in parking_lot:
        print(current_plate)

else:
    print("Parking Lot is Empty")

