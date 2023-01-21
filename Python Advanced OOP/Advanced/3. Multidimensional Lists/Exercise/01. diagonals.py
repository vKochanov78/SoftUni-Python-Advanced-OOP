num = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(num)]

primary_diagonal = [matrix[r][r] for r in range(num)]
secondary_diagonal = [matrix[r][num - r - 1] for r in range(num - 1, -1, -1)]

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal[::-1])}. Sum: {sum(secondary_diagonal)}')

