numbers = [int(x) for x in input().split()]
positive_numbers_sum = sum(num for num in numbers if num > 0)
negative_numbers_sum = sum(num for num in numbers if num < 0)

print(negative_numbers_sum)
print(positive_numbers_sum)

if abs(negative_numbers_sum) > positive_numbers_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")