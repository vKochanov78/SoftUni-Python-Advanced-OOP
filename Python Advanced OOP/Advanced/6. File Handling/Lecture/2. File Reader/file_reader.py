try:
    file = open("numbers.txt", "r")
    sum_of_numbers = 0

    for current_number in file:
        sum_of_numbers += int(current_number)

    print(sum_of_numbers)

except FileNotFoundError as err:
    print(err)


# You are given a file called numbers.txt with the following content:

# 1  2  3  4  5

# Create a program that reads the numbers from the file.
# Print on the console the sum of those numbers.