        # Given code to work on.

# numbers_dictionary = {}
#
# line = input()
#
# while line != "Search":
#     number_as_string = line
#     number = int(input())
#     numbers_dictionary[number_as_string] = number
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     print(numbers_dictionary[searched])
#
# line = input()
#
# while line != "End":
#     searched = line
#     del numbers_dictionary[searched]
#
# print(numbers_dictionary)

        # After i had finished working on it.

numbers_dictionary = {}

line = input()

while line != "Search":
    try:
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()

while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()

while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]

    except KeyError:
        print("Number does not exist in dictionary")

    line = input()


print(numbers_dictionary)


    # Input lines:
  #1st      2nd         3rd
# one       one         one
# 1         two         1
# two       Search      Search
# 2         Remove      one
# Search    End         Remove
# one                   two
# Remove                End
# two
# End