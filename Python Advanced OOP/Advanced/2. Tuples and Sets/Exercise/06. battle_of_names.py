even_set = set()
odd_set = set()

for current_row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(letter) for letter in input()) // current_row

    if ascii_sum_of_name % 2 == 0:
        even_set.add(ascii_sum_of_name)

    else:
        odd_set.add(ascii_sum_of_name)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=", ")

elif sum(even_set) < sum (odd_set):
    print(*odd_set.difference(even_set), sep=", ")

else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")

