        # The given code is:

# numbers_list = int(input()).split(", ")
# result = 1
#
# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number <= 5
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(total)

        # Inputs #
    # 2, 5, 10
    # 4, 5, 6, 1, 3
    # 1, 4, 5
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11


            #  The code when i fixed it.

numbers_list = [int(x) for x in input().split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)