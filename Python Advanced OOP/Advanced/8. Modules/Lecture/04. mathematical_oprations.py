from modules import operations

while True:
    try:
        data = operations(*input('Enter: first num, operator, second num: ').split(" "))
        print(f"Result is: {data}")
        break

    except ValueError:
        print("Enter valid data")