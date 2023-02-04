class ValueCannotBeNegative(Exception):
    pass


for i in range(1, 6):
    number = int(input())

    if number < 0:
        raise ValueCannotBeNegative(f"You should enter a positive number"'\n'
                f"{32 * ' '}Convert number {number} to {abs(number)}")

