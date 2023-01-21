from functools import reduce

expression = input().split()

functions_map = {
    '*': lambda i: reduce(lambda a, b: int(a) * int(b), expression[:i]),
    '/': lambda i: reduce(lambda a, b: int(a) / int(b), expression[:i]),
    '+': lambda i: reduce(lambda a, b: int(a) + int(b), expression[:i]),
    '-': lambda i: reduce(lambda a, b: int(a) - int(b), expression[:i]),
}

index = 0

while len(expression) > index:

    element = expression[index]

    if element in '*+/-':
        result = functions_map[element](index)
        [expression.pop(1) for el in range(index)]
        expression[0] = result
        index = 0

    index += 1

print(int(expression[0]))
