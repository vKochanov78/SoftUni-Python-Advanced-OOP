def operate(operator, *args):
    result = args[0]

    if operator == "+":
        result = sum(args)
    elif operator == "-":
        for number in args[1:]:
            result -= number
    elif operator == "*":
        for number in args[1:]:
            result *= number
    elif operator == "/":
        for number in args[1:]:
            result /= number

    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 17, 12, 3))
print(operate("/", 20, 5, 2))