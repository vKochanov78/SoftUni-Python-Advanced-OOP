def multiply(*args):
    product = 1

    for number in args:
        product *= number

    return product

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))