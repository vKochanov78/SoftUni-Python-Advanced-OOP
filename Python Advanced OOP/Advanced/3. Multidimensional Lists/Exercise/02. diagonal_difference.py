num = int(input())
matrix = [[int(r) for r in input().split()] for _ in range(num)]

primary_diagonal = [matrix[r][r] for r in range(num)]
secondary_diagonal = [matrix[r][num - r - 1] for r in range(num -1, -1, -1)]

diff = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diff)